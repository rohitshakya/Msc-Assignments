%{ 
   /* Definition section */
  #include<stdio.h> 
  #include "y.tab.h" 
  void yyerror(char *s);
%} 
  
/* Rule Section */
%% 
[0-9]+ { 
          yylval=atoi(yytext); 
          return NUM; 
  
       } 
[\t] ; 
  
[\n] return 0; 
  
. return yytext[0]; 
  
%% 
  
int yywrap() 
{ 
 return 1; 
} 

