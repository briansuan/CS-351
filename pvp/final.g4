grammar final;

start : expr1 | expr2 | <EOF> ;

expr1 : 'duration' duration=NUMBER #get_duration;
expr2 : '->' players=PLAYER        #get_players;

NUMBER : ('0'..'9')+;
PLAYER : ('0'..'9' | 'a'..'z' | 'A'..'Z')+;
WS     : [ \r\n\t]+ -> skip; 

