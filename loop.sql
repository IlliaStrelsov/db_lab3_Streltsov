DO $$
 DECLARE
     company_id   companies.company_id%TYPE;
     company_name companies.company_name%TYPE;
 BEGIN
     company_id := 10;
     company_name := 'Simple game';
     FOR counter IN 1..10
         LOOP
             INSERT INTO companies(company_id, company_name)
            VALUES (counter + company_id, company_name || counter);
         END LOOP;
 END;
 $$
