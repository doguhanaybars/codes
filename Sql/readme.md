You run some samples interactively from SQL*Plus, others from Pro*C programs. You can experiment with the samples from any Oracle account. However, the Pro*C examples expect you to use the scott/tiger account.

Before trying the samples, you must create some database tables, then load the tables with data. You do that by running two SQL*Plus scripts, exampbld and examplod, which are supplied with PL/SQL. You can find these scripts in the PL/SQL demo directory.

The first script builds the database tables processed by the sample programs. The second script loads (or reloads) the database tables. To run the scripts, invoke SQL*Plus, then issue the following commands:

SQL> START exampbld
...
SQL> START examplod
<h1>Sample 1. FOR Loop</h1>
The following example uses a simple FOR loop to insert ten rows into a database table. The values of a loop index, counter variable, and either of two character strings are inserted. Which string is inserted depends on the value of the loop index.

<h2>Input Table</h2>
Not applicable.

<h2>PL/SQL Block</h2>
-- available online in file 'sample1'
DECLARE
   x NUMBER := 100;
BEGIN
   FOR i IN 1..10 LOOP
      IF MOD(i,2) = 0 THEN     -- i is even
         INSERT INTO temp VALUES (i, x, 'i is even');
      ELSE
         INSERT INTO temp VALUES (i, x, 'i is odd');
      END IF;
      x := x + 100;
   END LOOP;
   COMMIT;
END;
<h2>Output Table</h2>
...
SQL> SELECT * FROM temp ORDER BY col1;
...
NUM_COL1 NUM_COL2  CHAR_COL
-------- --------  ---------
       1      100  i is odd
       2      200  i is even
       3      300  i is odd
       4      400  i is even
       5      500  i is odd
       6      600  i is even
       7      700  i is odd
       8      800  i is even
       9      900  i is odd
      10     1000  i is even
<h1>Sample 2. Cursors</h1>
The following example uses a cursor to select the five highest paid employees from the emp table.

<h2>Input Table</h2>
SQL> SELECT ename, empno, sal FROM emp ORDER BY sal DESC;

ENAME          EMPNO      SAL
---------- --------- --------
KING            7839     5000
SCOTT           7788     3000
FORD            7902     3000
JONES           7566     2975
BLAKE           7698     2850
CLARK           7782     2450
ALLEN           7499     1600
TURNER          7844     1500
MILLER          7934     1300
WARD            7521     1250
MARTIN          7654     1250
ADAMS           7876     1100
JAMES           7900      950
SMITH           7369      800
<h2>PL/SQL Block</h2>
-- available online in file 'sample2'
DECLARE
   CURSOR c1 is
      SELECT ename, empno, sal FROM emp
         ORDER BY sal DESC;   -- start with highest paid employee
   my_ename VARCHAR2(10);
   my_empno NUMBER(4);
   my_sal   NUMBER(7,2);
BEGIN
   OPEN c1;
   FOR i IN 1..5 LOOP
      FETCH c1 INTO my_ename, my_empno, my_sal;
      EXIT WHEN c1%NOTFOUND;  /* in case the number requested */
                              /* is more than the total       */
                              /* number of employees          */
      INSERT INTO temp VALUES (my_sal, my_empno, my_ename);
      COMMIT;
   END LOOP;
   CLOSE c1;
END;
<h2>Output Table</h2>
SQL> SELECT * FROM temp ORDER BY col1 DESC;

NUM_COL1 NUM_COL2  CHAR_COL
-------- --------  --------
    5000     7839  KING
    3000     7902  FORD
    3000     7788  SCOTT
    2975     7566  JONES
    2850     7698  BLAKE
<h1>Sample 3. Scoping</h1>
The following example illustrates block structure and scope rules. An outer block declares two variables named x and counter and loops four times. Inside this loop is a sub-block that also declares a variable named x. The values inserted into the temp table show that the two x's are indeed different.

<h2>Input Table</h2>
Not applicable.

<h2>PL/SQL Block</h2>
-- available online in file 'sample3'
DECLARE
   x NUMBER := 0;
   counter NUMBER := 0;
BEGIN
   FOR i IN 1..4 LOOP
      x := x + 1000;
      counter := counter + 1;
      INSERT INTO temp VALUES (x, counter, 'in OUTER loop');
      /* start an inner block */
      DECLARE
         x NUMBER := 0;  -- this is a local version of x
      BEGIN
         FOR i IN 1..4 LOOP
            x := x + 1;  -- this increments the local x
            counter := counter + 1;
            INSERT INTO temp VALUES (x, counter, 'inner loop');
         END LOOP;
      END;
   END LOOP;
   COMMIT;
END;
<h2>Output Table</h2>
SQL> SELECT * FROM temp ORDER BY col2;

NUM_COL1 NUM_COL2  CHAR_COL
-------- --------  -------------
    1000        1  in OUTER loop
       1        2  inner loop
       2        3  inner loop
       3        4  inner loop
       4        5  inner loop
    2000        6  in OUTER loop
       1        7  inner loop
       2        8  inner loop
       3        9  inner loop
       4       10  inner loop
    3000       11  in OUTER loop
       1       12  inner loop
       2       13  inner loop
       3       14  inner loop
      4        15  inner loop
    4000       16  in OUTER loop
       1       17  inner loop
       2       18  inner loop
       3       19  inner loop
       4       20  inner loop
<h1>Sample 4. Batch Transaction Processing</h1>
In the next example the accounts table is modified according to instructions stored in the action table. Each row in the action table contains an account number, an action to be taken (I, U, or D for insert, update, or delete), an amount by which to update the account, and a time tag used to sequence the transactions.

On an insert, if the account already exists, an update is done instead. On an update, if the account does not exist, it is created by an insert. On a delete, if the row does not exist, no action is taken.

<h2>Input Tables</h2>
SQL> SELECT * FROM accounts ORDER BY account_id;

ACCOUNT_ID     BAL
---------- -------
         1    1000
         2    2000
         3    1500
         4    6500
         5     500

SQL> SELECT * FROM action ORDER BY time_tag;

ACCOUNT_ID  O  NEW_VALUE STATUS                TIME_TAG
----------  - ---------- -------------------- ---------
         3  u        599                      18-NOV-88
         6  i      20099                      18-NOV-88
         5  d                                 18-NOV-88
         7  u       1599                      18-NOV-88
         1  i        399                      18-NOV-88
         9  d                                 18-NOV-88
        10  x                                 18-NOV-88
<h2>PL/SQL Block</h2>
-- available online in file 'sample4'
DECLARE
   CURSOR c1 IS
      SELECT account_id, oper_type, new_value FROM action
      ORDER BY time_tag
      FOR UPDATE OF status;
BEGIN
   FOR acct IN c1 LOOP  -- process each row one at a time

   acct.oper_type := upper(acct.oper_type);

   /*----------------------------------------*/
   /* Process an UPDATE.  If the account to  */
   /* be updated doesn't exist, create a new */
   /* account.                               */
   /*----------------------------------------*/
   IF acct.oper_type = 'U' THEN
      UPDATE accounts SET bal = acct.new_value
         WHERE account_id = acct.account_id;

      IF SQL%NOTFOUND THEN  -- account didn't exist. Create it.
         INSERT INTO accounts
            VALUES (acct.account_id, acct.new_value);
         UPDATE action SET status =
            'Update: ID not found. Value inserted.'
            WHERE CURRENT OF c1;
      ELSE
         UPDATE action SET status = 'Update: Success.'
            WHERE CURRENT OF c1;
      END IF;

   /*--------------------------------------------*/
   /* Process an INSERT.  If the account already */
   /* exists, do an update of the account        */
   /* instead.                                   */
   /*--------------------------------------------*/
   ELSIF acct.oper_type = 'I' THEN
      BEGIN
         INSERT INTO accounts
            VALUES (acct.account_id, acct.new_value);
         UPDATE action set status = 'Insert: Success.'
            WHERE CURRENT OF c1;
         EXCEPTION
            WHEN DUP_VAL_ON_INDEX THEN   -- account already exists
               UPDATE accounts SET bal = acct.new_value
                  WHERE account_id = acct.account_id;
               UPDATE action SET status =
                  'Insert: Acct exists. Updated instead.'
                  WHERE CURRENT OF c1;
       END;

   /*--------------------------------------------*/
   /* Process a DELETE.  If the account doesn't  */
   /* exist, set the status field to say that    */
   /* the account wasn't found.                  */
   /*--------------------------------------------*/
   ELSIF acct.oper_type = 'D' THEN
      DELETE FROM accounts
         WHERE account_id = acct.account_id;

      IF SQL%NOTFOUND THEN   -- account didn't exist.
         UPDATE action SET status = 'Delete: ID not found.'
            WHERE CURRENT OF c1;
      ELSE
         UPDATE action SET status = 'Delete: Success.'
            WHERE CURRENT OF c1;
      END IF;
  
   /*--------------------------------------------*/
   /* The requested operation is invalid.        */
   /*--------------------------------------------*/
   ELSE  -- oper_type is invalid
      UPDATE action SET status =
         'Invalid operation. No action taken.'
         WHERE CURRENT OF c1;

   END IF;

   END LOOP;
   COMMIT;
END;
<h2>Output Tables</h2>
SQL> SELECT * FROM accounts ORDER BY account_id;

ACCOUNT_ID      BAL
---------- --------
         1      399
         2     2000
         3      599
         4     6500
         6    20099
         7     1599

SQL> SELECT * FROM action ORDER BY time_tag;

ACCOUNT_ID  O  NEW_VALUE STATUS                  TIME_TAG
----------  - ---------- ---------------------  ---------
         3  u        599 Update: Success.       18-NOV-88
         6  i      20099 Insert: Success.       18-NOV-88
         5  d            Delete: Success.       18-NOV-88
         7  u       1599 Update: ID not found.  18-NOV-88
                         Value inserted.
         1  i        399 Insert: Acct exists.   18-NOV-88
                         Updated instead.
         9  d            Delete: ID not found.  18-NOV-88
        10  x            Invalid operation.     18-NOV-88
                         No action taken.
<h1>Sample 5. Embedded PL/SQL</h1>
The following example shows how you can embed PL/SQL in a high-level host language such as C and demonstrates how a banking debit transaction might be done.

<h2>Input Table</h2>
SQL> SELECT * FROM accounts ORDER BY account_id;

ACCOUNT_ID      BAL
---------- --------
         1     1000
         2     2000
         3     1500
         4     6500
         5      500
<h2>PL/SQL Block in a C Program</h2>
/* available online in file 'sample5' */
#include <stdio.h>
   char    buf[20];
EXEC SQL BEGIN DECLARE SECTION;
   int     acct;
   double  debit;
   double  new_bal;
   VARCHAR status[65];
   VARCHAR uid[20];
   VARCHAR pwd[20];
EXEC SQL END DECLARE SECTION;

EXEC SQL INCLUDE SQLCA;

main()
{
   extern double atof();

   strcpy (uid.arr,"scott");
   uid.len=strlen(uid.arr);
   strcpy (pwd.arr,"tiger");
   pwd.len=strlen(pwd.arr);

   printf("\n\n\tEmbedded PL/SQL Debit Transaction Demo\n\n");
   printf("Trying to connect...");
   EXEC SQL WHENEVER SQLERROR GOTO errprint;
   EXEC SQL CONNECT :uid IDENTIFIED BY :pwd;
   printf(" connected.\n");
for (;;)       /*  Loop infinitely */
{
   printf("\n** Debit which account number? (-1 to end) ");
   gets(buf);
   acct = atoi(buf);
   if (acct == -1)  /* Need to disconnect from Oracle */
   {                /* and exit loop if account is -1 */
       EXEC SQL COMMIT RELEASE;
       exit(0);
   }

   printf("   What is the debit amount? ");
   gets(buf);
   debit = atof(buf);

   /* ---------------------------------- */
   /* ----- Begin the PL/SQL block ----- */
   /* ---------------------------------- */
   EXEC SQL EXECUTE

   DECLARE
      insufficient_funds EXCEPTION;
      old_bal            NUMBER;
      min_bal            CONSTANT NUMBER := 500;
   BEGIN
      SELECT bal INTO old_bal FROM accounts
         WHERE account_id = :acct;
         -- If the account doesn't exist, the NO_DATA_FOUND
         -- exception will be automatically raised.
      :new_bal := old_bal - :debit;
      IF :new_bal >= min_bal THEN
         UPDATE accounts SET bal = :new_bal
            WHERE account_id = :acct;
         INSERT INTO journal
            VALUES (:acct, 'Debit', :debit, SYSDATE);
         :status := 'Transaction completed.';
      ELSE
         RAISE insufficient_funds;
      END IF;
      COMMIT;
   EXCEPTION
      WHEN NO_DATA_FOUND THEN
         :status := 'Account not found.';
         :new_bal := -1;
      WHEN insufficient_funds THEN
         :status := 'Insufficient funds.';
         :new_bal := old_bal;
      WHEN OTHERS THEN
         ROLLBACK;
         :status := 'Error: ' || SQLERRM(SQLCODE);
         :new_bal := -1;
   END;
  
   END-EXEC;
   /* -------------------------------- */
   /* ----- End the PL/SQL block ----- */
   /* -------------------------------- */

   status.arr[status.len] = '\0';  /* null-terminate */
                                   /* the string     */
   printf("\n\n   Status:  %s\n", status.arr);
   if (new_bal >= 0)
      printf("   Balance is now:  $%.2f\n", new_bal);
}  /* End of loop */

errprint:
   EXEC SQL WHENEVER SQLERROR CONTINUE;
   printf("\n\n>>>>> Error during execution:\n");
   printf("%s\n",sqlca.sqlerrm.sqlerrmc);
   EXEC SQL ROLLBACK RELEASE;
   exit(1);
}
<h2>Interactive Session</h2>
Embedded PL/SQL Debit Transaction Demo

Trying to connect... connected.
  
** Debit which account number? (-1 to end) 1
   What is the debit amount? 300

   Status:  Transaction completed.
   Balance is now:  $700.00

** Debit which account number? (-1 to end) 1
   What is the debit amount? 900
   Status:  Insufficient funds.
   Balance is now:  $700.00

** Debit which account number? (-1 to end) 2
   What is the debit amount? 500

   Status:  Transaction completed.
   Balance is now:  $1500.00

** Debit which account number? (-1 to end) 2
   What is the debit amount? 100

   Status:  Transaction completed.
   Balance is now:  $1400.00

** Debit which account number? (-1 to end) 99
   What is the debit amount? 100

   Status:  Account not found.

** Debit which account number? (-1 to end) -1
<h2>Output Tables</h2>
SQL> SELECT * FROM accounts ORDER BY account_id;

ACCOUNT_ID    BAL
---------- ------
         1    700
         2   1400
         3   1500
         4   6500
         5    500

SQL> SELECT * FROM journal ORDER BY date_tag;

ACCOUNT_ID  ACTION                   AMOUNT   DATE_TAG
----------  --------------------  ---------  ---------
         1  Debit                       300  28-NOV-88
         2  Debit                       500  28-NOV-88
         2  Debit                       100  28-NOV-88
<h1>Sample 6. Calling a Stored Procedure</h1>
This Pro*C program connects to Oracle, prompts the user for a department number, then calls procedure get_employees, which is stored in package personnel. The procedure declares three index-by tables as OUT formal parameters, then fetches a batch of employee data into the index-by tables. The matching actual parameters are host arrays.

When the procedure finishes, it automatically assigns all row values in the index-by tables to corresponding elements in the host arrays. The program calls the procedure repeatedly, displaying each batch of employee data, until no more data is found.

<h2>Input Table</h2>
SQL> SELECT ename, empno, sal FROM emp ORDER BY sal DESC;

ENAME          EMPNO      SAL
---------- --------- --------
KING            7839     5000
SCOTT           7788     3000
FORD            7902     3000
JONES           7566     2975
BLAKE           7698     2850
CLARK           7782     2450
ALLEN           7499     1600
TURNER          7844     1500
MILLER          7934     1300
WARD            7521     1250
MARTIN          7654     1250
ADAMS           7876     1100
JAMES           7900      950
SMITH           7369      800
<h2>Stored Procedure</h2>
/* available online in file 'sample6' */
#include <stdio.h>
#include <string.h>

typedef char asciz;

EXEC SQL BEGIN DECLARE SECTION;
   /* Define type for null-terminated strings. */
   EXEC SQL TYPE asciz IS STRING(20);
   asciz  username[20];
   asciz  password[20];
   int    dept_no;    /* which department to query */
   char   emp_name[10][21];
   char   job[10][21];
   EXEC SQL VAR emp_name is STRING (21);
   EXEC SQL VAR job is STRING (21);
   float  salary[10];
   int    done_flag;
   int    array_size;
   int    num_ret;    /* number of rows returned */
   int    SQLCODE;
EXEC SQL END DECLARE SECTION;

EXEC SQL INCLUDE sqlca;

int print_rows();       /* produces program output      */
int sqlerror();         /* handles unrecoverable errors */

main()
{
   int i;

   /* Connect to Oracle. */
   strcpy(username, "SCOTT");
   strcpy(password, "TIGER");

   EXEC SQL WHENEVER SQLERROR DO sqlerror();

   EXEC SQL CONNECT :username IDENTIFIED BY :password;
   printf("\nConnected to Oracle as user: %s\n\n", username);

   printf("Enter department number: ");
   scanf("%d", &dept_no);
   fflush(stdin);

   /* Print column headers. */
   printf("\n\n");
   printf("%-10.10s%-10.10s%s\n", "Employee", "Job", "Salary");
   printf("%-10.10s%-10.10s%s\n", "--------", "---", "------");

   /* Set the array size. */
   array_size = 10;
   done_flag = 0;
   num_ret = 0;

   /* Array fetch loop - ends when NOT FOUND becomes true. */
   for (;;)
   {
      EXEC SQL EXECUTE
         BEGIN personnel.get_employees
            (:dept_no, :array_size, :num_ret, :done_flag,
            :emp_name, :job, :salary);
         END;
      END-EXEC;

      print_rows(num_ret);

      if (done_flag)
         break;
   }

   /* Disconnect from Oracle. */
   EXEC SQL COMMIT WORK RELEASE;
   exit(0);
}

print_rows(n)
int n;
{
   int i;

   if (n == 0)
   {
      printf("No rows retrieved.\n");
      return;
   }

   for (i = 0; i < n; i++)
      printf("%10.10s%10.10s%6.2f\n",
         emp_name[i], job[i], salary[i]);
}
sqlerror()
{
   EXEC SQL WHENEVER SQLERROR CONTINUE;
   printf("\nOracle error detected:");
   printf("\n% .70s \n", sqlca.sqlerrm.sqlerrmc);
   EXEC SQL ROLLBACK WORK RELEASE;
   exit(1);
}
<h2>Interactive Session</h2>
Connected to Oracle as user: SCOTT

Enter department number: 20

Employee  Job       Salary
--------  ---       ------
SMITH     CLERK     800.00
JONES     MANAGER   2975.00
SCOTT     ANALYST   3000.00
ADAMS     CLERK     1100.00
FORD      ANALYST   3000.00
