








%{
    #include<stdio.h>
    int f=0;
%}

%token NUMBER
%token ID
%left '+' '-'
%left '*' '/'
%%
S:  E {printf("\n");}
    ;
E:  E '+' E {printf("+ ");}
    |   E '*' E {printf("* ");}
    |   E '-' E {printf("- ");}
    |   E '/' E {printf("/ ");}
    |   '(' E ')'
    |   NUMBER     {if(f==0){printf("Postfix Expression : ");f=1;} printf("%d ", yylval);}
    |   ID         {printf("%c ", yylval);}
    ;
%%

int main(){
    printf("\n*****************INFIX TO POSTFIX*****************\n");
    printf("Enter Infix Expression : ");
    yyparse();
    return 0;
}

int yyerror (char *msg) {
    return printf ("Invalid Infix Expression...");
}