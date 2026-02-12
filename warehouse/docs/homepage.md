{% docs __overview__ %}

### DBT-Core Project README

# DBT-Core Project for Commodities Data Warehouse

This project uses DBT (Data Build Tool) to manage and transform data from a commodities Data Warehouse (DW). The goal is to create a robust and efficient data pipeline that processes and organizes commodities data and its movements for analysis.

## Project Structure

```mermaid
graph TD
    A[Start] --> B[Extract Commodity Data]
    B --> C[Transform Commodity Data]
    C --> D[Load Data into PostgreSQL]
    D --> E[End]

    subgraph Extract
        B1[Search Data for Each Commodity]
        B2[Add Data to List]
    end

    subgraph Transform
        C1[Concatenate All Data]
        C2[Prepare DataFrame]
    end

    subgraph Load
        D1[Save DataFrame in PostgreSQL]
    end

    B --> B1
    B1 --> B2
    B2 --> C
    C --> C1
    C1 --> C2
    C2 --> D
    D --> D1
```

Translated with DeepL.com (free version)

### 1. Seeds

Seeds are static data that are loaded into the Data Warehouse from CSV files. In this project, we use seeds to load commodity movement data.

### 2. Models

Models define data transformations using SQL. They are divided into two main layers: staging and datamart.

#### Staging

The staging layer is responsible for preparing and cleaning the data before it is loaded into the final analysis tables.

- **stg_commodities.sql**: Processes and formats commodity data extracted from the API.
- **stg_movimentacao_commodities.sql**: Processes and formats commodity movement data.

#### Datamart

The datamart layer is where the final analysis data is stored. It is based on the data prepared by the staging layer.

- **dm_commodities.sql**: Integrates the processed commodity and movement data, creating a final data model for analysis.

### 3. Sources

Sources are the tables or files that contain the source data that DBT uses to perform transformations.
### 4. Snapshots

Snapshots are used to maintain a history of how data changes over time.

## Directory Structure

```plaintext
├── models
│   ├── staging
│   │   ├── stg_commodities.sql
│   │   └── stg_movimentacao_commodities.sql
│   └── datamart
│       └── dm_commodities.sql
├── seeds
│   └── movimentacao_commodities.csv
├── dbt_project.yml
└── README.md
```

## Running the Project

### Requirements

- Python 3.7+
- DBT

### Steps for Execution

1. **Clone the Repository**:
```bash
git clone <Repository-URL>
cd <Repository-Name>
```

2. **Install DBT:**
```bash
pip install dbt-core dbt-postgres
```
3. **Configure DBT:**
- Configure the `profiles.yml` file to connect to your Data Warehouse. The file should be in the `~/.dbt/` directory or in the directory specified by the `DBT_PROFILES_DIR` environment variable.

Example of `profiles.yml`:
```yaml
  databasesales:
    target: dev
    outputs:
      dev:
         type: postgres
         host: <DB_HOST_PROD>
         user: <DB_USER_PROD>
         password: <DB_PASS_PROD>
         port: <DB_PORT_PROD>
         dbname: <DB_NAME_PROD>
         schema: <DB_SCHEMA_PROD>
         threads: 1
   ```

4. **Run DBT Seeds:**
```bash
dbt seed
```

5. **Run DBT Transformations:**
```bash
dbt run
```
6. **Check Project Status**:
```bash
   dbt test
   ```

## Contribution

To contribute to the project, please fork the repository and send a pull request with your changes.

---

### Model Description

#### stg_commodities.sql

This model is responsible for processing and formatting commodity data extracted from the API. It performs the necessary cleaning and transformation to prepare the data for the datamart.

#### stg_movimentacao_commodities.sql

This model is responsible for processing and formatting commodity movement data. It performs the necessary cleaning and transformation to prepare the data for the datamart.

#### dm_commodities.sql

This model integrates the processed commodity and movement data, creating a final data model for analysis. It calculates metrics and aggregates the data to facilitate analysis in the dashboard.

{% enddocs %}


