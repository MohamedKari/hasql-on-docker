

# Docker MS SQL
```sh
docker compose up

# On the client
sqlcmd -S 0.0.0.0,1433 -U SA -P "Password1_"
```

```sql
CREATE DATABASE ProductCatalog
GO

USE ProductCatalog
CREATE TABLE Products (id INT, name NVARCHAR(50), gross_price DECIMAL)
INSERT INTO Products VALUES (1, 'smartphone', 799.99); 
INSERT INTO Products VALUES (2, 'tablet', 1099.99);
GO

SELECT * FROM Products WHERE gross_price > 500.0;
GO
```

# Check persistency
```sh
# kill the docker compose process
docker compose up

# In a new client session
sqlcmd -S 0.0.0.0,1433 -U SA -P "Password1_"
```

```sql
USE ProductCatalog
SELECT * FROM Products WHERE gross_price > 500.0;
GO
```


# Client Access
**Interactive**:
- VS Code

**CLI**:
- Containerized SQLCMD: https://hub.docker.com/_/microsoft-mssql-tools
- SQLCMD on MacOS: `brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release && brew update && brew install mssql-tools`
- MSSQL-CLI: https://github.com/dbcli/mssql-cli/blob/master/doc/installation/macos.md

**App**:
- Python: https://github.com/microsoft/mssql-docker/blob/master/oss-drivers/pyodbc/Dockerfile
- PHP: https://github.com/microsoft/mssql-docker/tree/master/oss-drivers/msphpsql
- NodeJS: https://github.com/microsoft/mssql-docker/tree/master/oss-drivers/tedious

# Tools

## MSSQL-TOOLS Container

## SQLCMD
```

```


## MSSQL-CLI

# Resources

- https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-setup-tools
- https://github.com/microsoft/mssql-docker


**MSSQL on K8s**
- **Demo**: https://docs.microsoft.com/en-us/sql/linux/quickstart-install-connect-docker
- **Tutorial**: https://docs.microsoft.com/en-us/sql/linux/tutorial-sql-server-containers-kubernetes
- **Helm Chart** https://github.com/microsoft/mssql-docker/tree/master/linux/sample-helm-chart

**HA**
- https://www.sqlservercentral.com/articles/sql-server-alwayson-with-docker-containers

**Custom DB Setup**
- https://github.com/microsoft/mssql-docker/tree/master/linux/preview/examples/mssql-customize


- Environment Variables: https://docs.microsoft.com/en-us/sql/linux/sql-server-linux-configure-environment-variables?view=sql-server-ver15

