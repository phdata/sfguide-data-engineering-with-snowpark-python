
-- ----------------------------------------------------------------------------
-- Step #1: Accept Anaconda Terms & Conditions
-- ----------------------------------------------------------------------------

-- See Getting Started section in Third-Party Packages (https://docs.snowflake.com/en/developer-guide/udf/python/udf-python-packages.html#getting-started)


-- ----------------------------------------------------------------------------
-- Step #2: Create the account level objects
-- ----------------------------------------------------------------------------
SET ORIGINAL_ROLE = CURRENT_ROLE();

USE ROLE ACCOUNTADMIN;

-- Roles
SET MY_USER = CURRENT_USER();

GRANT EXECUTE TASK ON ACCOUNT TO ROLE DBA2;
GRANT MONITOR EXECUTION ON ACCOUNT TO ROLE DBA2;
GRANT IMPORTED PRIVILEGES ON DATABASE SNOWFLAKE TO ROLE DBA2;


-- Databases
CREATE OR REPLACE DATABASE HOL_DB2;
GRANT OWNERSHIP ON DATABASE HOL_DB2 TO ROLE DBA2;

-- ----------------------------------------------------------------------------
-- Step #3: Add Frostbyte Weathersource data to account.
-- ----------------------------------------------------------------------------
GRANT IMPORTED PRIVILEGES ON DATABASE FROSTBYTE_WEATHERSOURCE TO ROLE DBA2;

USE ROLE IDENTIFIER($ORIGINAL_ROLE);
