import random



def init():
    return ("⚰️")

def run(db_cursor , state):

    # Get all my dots
    rows = db_cursor.execute(f"select x,y from main_game_field as gf, owner where is_flag = FALSE "
                             f"and gf.owner_id = owner.owner_id and owner.name = '{state['NAME']}'")
    # Fetch all dots
    dots = rows.fetchall()


    for row in dots:
        # Get nearest food location
        food = db_cursor.execute(
            f"""
            select x,y from main_game_field as gf, owner where is_flag = FALSE
            and gf.owner_id != owner.owner_id and owner.name = 'Food'
            order by sqrt(pow({row[0]} - x, 2) + pow({row[1]} - y, 2))
            """
        )

        # Get nearest enemy location
        enemies = db_cursor.execute(

            f"""
            select x,y from main_game_field as gf, owner where
            gf.owner_id = owner.owner_id and owner.name != '{state['NAME']}'
            and owner.name != 'Food'
            order by sqrt(pow({row[0]} - x, 2) + pow({row[1]} - y, 2))
            """
        )

        try:
            # Get x,y of food
            food_x = food.fetchone()[0]
            food_y = food.fetchone()[1]
            # Get x,y of enemies
            enemy_x = enemies.fetchone()[0]
            enemy_y = enemies.fetchone()[1]
        except TypeError:
            return None


        ### BOUND CHECK: If a dot is at a bound, bounce off in any direction ###
        bounce_path = random.random()
        # x-Left bound
        if row[0] == 0:
            if bounce_path < 0.33:
                db_cursor.execute(f"insert into engine_orders values("
                                  f"{row[0]}, {row[1]}, {row[0] + 1}, {row[1] - 1}, 'MOVE')")
            elif 0.33 <= bounce_path <= 0.66:
                db_cursor.execute(f"insert into engine_orders values("
                                  f"{row[0]}, {row[1]}, {row[0] + 1}, {row[1] + 1}, 'MOVE')")
            elif bounce_path > 0.66:
                db_cursor.execute(f"insert into engine_orders values("
                                  f"{row[0]}, {row[1]}, {row[0] + 1}, {row[1]}, 'MOVE')")
        # x-Right bound
        elif row[0] == state['MAX_X'] - 1:
            if bounce_path < 0.33:
                db_cursor.execute(f"insert into engine_orders values("
                                  f"{row[0]}, {row[1]}, {row[0] - 1}, {row[1] + 1}, 'MOVE')")
            elif 0.33 <= bounce_path <= 0.66:
                db_cursor.execute(f"insert into engine_orders values("
                                  f"{row[0]}, {row[1]}, {row[0] - 1}, {row[1] - 1}, 'MOVE')")
            elif bounce_path > 0.66:
                db_cursor.execute(f"insert into engine_orders values("
                                  f"{row[0]}, {row[1]}, {row[0] - 1}, {row[1]}, 'MOVE')")
        # y-Bottom bound
        elif row[1] == state['MAX_Y'] - 1:
            if bounce_path < 0.33:
                db_cursor.execute(f"insert into engine_orders values("
                                  f"{row[0]}, {row[1]}, {row[0] - 1}, {row[1] - 1}, 'MOVE')")
            elif 0.33 <= bounce_path <= 0.66:
                db_cursor.execute(f"insert into engine_orders values("
                                  f"{row[0]}, {row[1]}, {row[0] + 1}, {row[1] - 1}, 'MOVE')")
            elif bounce_path > 0.66:
                db_cursor.execute(f"insert into engine_orders values("
                                  f"{row[0]}, {row[1]}, {row[0]}, {row[1] - 1}, 'MOVE')")
        # y-Top bound
        elif row[1] == 0:
            if bounce_path < 0.33:
                db_cursor.execute(f"insert into engine_orders values("
                                  f"{row[0]}, {row[1]}, {row[0] - 1}, {row[1] + 1}, 'MOVE')")
            elif 0.33 <= bounce_path <= 0.66:
                db_cursor.execute(f"insert into engine_orders values("
                                  f"{row[0]}, {row[1]}, {row[0] + 1}, {row[1] + 1}, 'MOVE')")
            elif bounce_path > 0.66:
                db_cursor.execute(f"insert into engine_orders values("
                                  f"{row[0]}, {row[1]}, {row[0]}, {row[1] + 1}, 'MOVE')")

        ### MAIN STRATEGY ###
        # If I have 6 or less dots, just find food
        if len(dots) <= 8:
            # call eat() to find food
            eat(food_x, food_y, row[0], row[1], db_cursor)

        # Otherwise, if I have more than 6 dots, make 65 % of newly created dots hunt for enemies
        # and make remaining 35% eat food
        else:
            if random.random() > 0.5:
                # Call hunt() to find enemies
                hunt(enemy_x, enemy_y, row[0], row[1], db_cursor)
            else:
                # If within 0.35, find food
                eat(food_x, food_y, row[0], row[1], db_cursor)



### Function to eat food ###
def eat(x_food, y_food, me_x, me_y, cursor):
    # Food is below me
    if x_food == me_x and y_food > me_y:
        cursor.execute(f"insert into engine_orders values("
                       f"{me_x}, {me_y}, {me_x}, {me_y + 1}, 'MOVE')")
    # Food is above of me
    elif x_food == me_x and y_food < me_y:
        cursor.execute(f"insert into engine_orders values("
                       f"{me_x}, {me_y}, {me_x}, {me_y - 1}, 'MOVE')")
    # Food is to my left
    elif x_food < me_x and y_food == me_y:
        cursor.execute(f"insert into engine_orders values("
                       f"{me_x}, {me_y}, {me_x - 1}, {me_y}, 'MOVE')")
    # Food is to my right
    elif x_food > me_x and y_food == me_y:
        cursor.execute(f"insert into engine_orders values("
                       f"{me_x}, {me_y}, {me_x + 1}, {me_y}, 'MOVE')")
    # Food is upper left
    elif x_food < me_x and y_food < me_y:
        cursor.execute(f"insert into engine_orders values("
                       f"{me_x}, {me_y}, {me_x - 1}, {me_y - 1}, 'MOVE')")
    # Food is upper right
    elif x_food > me_x and y_food < me_y:
        cursor.execute(f"insert into engine_orders values("
                       f"{me_x}, {me_y}, {me_x + 1}, {me_y - 1}, 'MOVE')")
    # Food is bottom left
    elif x_food < me_x and y_food > me_y:
        cursor.execute(f"insert into engine_orders values("
                       f"{me_x}, {me_y}, {me_x - 1}, {me_y + 1}, 'MOVE')")
    # Food is bottom right
    elif x_food > me_x and y_food > me_y:
        cursor.execute(f"insert into engine_orders values("
                       f"{me_x}, {me_y}, {me_x + 1}, {me_y + 1}, 'MOVE')")

### Function to find enemies ###
def hunt(op_x, op_y, my_x, my_y, cursor):
    # enemy is below me
    if op_x == my_x and op_y > my_y:
        cursor.execute(f"insert into engine_orders values("
                       f"{my_x}, {my_y}, {my_x}, {my_y + 1}, 'MOVE')")
    # enemy is above of me
    elif op_x == my_x and op_y < my_y:
        cursor.execute(f"insert into engine_orders values("
                       f"{my_x}, {my_y}, {my_x}, {my_y - 1}, 'MOVE')")
    # enemy is to my left
    elif op_x < my_x and op_y == my_y:
        cursor.execute(f"insert into engine_orders values("
                       f"{my_x}, {my_y}, {my_x - 1}, {my_y}, 'MOVE')")
    # enemy is to my right
    elif op_x > my_x and op_y == my_y:
        cursor.execute(f"insert into engine_orders values("
                       f"{my_x}, {my_y}, {my_x + 1}, {my_y}, 'MOVE')")
    # enemy is upper left
    elif op_x < my_x and op_y < my_y:
        cursor.execute(f"insert into engine_orders values("
                       f"{my_x}, {my_y}, {my_x - 1}, {my_y - 1}, 'MOVE')")
    # enemy is upper right
    elif op_x > my_x and op_y < my_y:
        cursor.execute(f"insert into engine_orders values("
                       f"{my_x}, {my_y}, {my_x + 1}, {my_y - 1}, 'MOVE')")
    # enemy is bottom left
    elif op_x < my_x and op_y > my_y:
        cursor.execute(f"insert into engine_orders values("
                       f"{my_x}, {my_y}, {my_x - 1}, {my_y + 1}, 'MOVE')")
    # enemy is bottom right
    elif op_x > my_x and op_y > my_y:
        cursor.execute(f"insert into engine_orders values("
                       f"{my_x}, {my_y}, {my_x + 1}, {my_y + 1}, 'MOVE')")

































