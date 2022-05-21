grammar gcode;

start : expr | <EOF> ;

expr     : 'G01' x_cord=NUMBER y_cord=NUMBER #draw_G01    
         | 'G02' rad=NUMBER ext=NUMBER #draw_G02    
         | 'G28' x_cord=NUMBER y_cord=NUMBER #draw_G28
         ;
NUMBER : (NEG? ('0' .. '9')+) (NEG? ('.' ('0' .. '9'))+)?;
NEG : '-';
WS : [ \r\n\t]+ -> skip;
































