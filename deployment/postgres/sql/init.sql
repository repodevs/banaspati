CREATE USER banaspatidbuser;
CREATE DATABASE banaspatidbprod;
CREATE DATABASE banaspatidbdev;
CREATE DATABASE banaspatidbtest;
GRANT ALL PRIVILEGES ON DATABASE banaspatidbprod TO banaspatidbuser;
GRANT ALL PRIVILEGES ON DATABASE banaspatidbdev TO banaspatidbuser;
GRANT ALL PRIVILEGES ON DATABASE banaspatidbtest TO banaspatidbuser;