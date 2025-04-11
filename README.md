

This schema is designed to support analytical queries on the Bank Marketing Dataset from Kaggle. The schema follows a star schema pattern to normalize the data and optimize it for reporting and dashboarding purposes.

# Dimension Tables

# client table
Stores demographic information about clients.

| Column Name     | Data Type | Description                         |
|-----------------|-----------|-------------------------------------|
| client_id       | INT (PK)  | Unique identifier for each client   |
| age             | INT       | Age of the client                   |
| job             | STRING    | Type of job                         |
| marital         | STRING    | Marital status                      |
| education       | STRING    | Education level                     |
| credit_default  | STRING    | Credit default status               |
| housing         | STRING    | Housing loan status                 |
| loan            | STRING    | Personal loan status                |
| age_group       | STRING    | Age group (e.g., 25–34)             |


# contact table
Stores contact-related campaign information.

| Column Name       | Data Type | Description                         |
|-------------------|-----------|-------------------------------------|
| contact_id        | INT (PK)  | Unique identifier for each contact  |
| contact           | STRING    | Contact communication type          |
| month             | STRING    | Last contact month                  |
| day               | STRING    | Last contact day                    |
| duration          | INT       | Call duration in seconds            |
| duration_length   | STRING    | Duration (Short/Medium/Long)        |

---

# campaign table
Holds historical campaign interaction data.

| Column Name   | Data Type | Description                              |
|---------------|-----------|------------------------------------------|
| campaign_id   | INT (PK)  | Unique campaign identifier               |
| campaign      | INT       | Number of contacts during campaign       |
| pdays         | INT       | Days since last contact                  |
| previous      | INT       | Number of contacts before this campaign  |
| poutcome      | STRING    | Outcome of previous campaign             |


# Fact Table

# fact_campaign_results table
Captures the outcome of marketing campaigns.

| Column Name   | Data Type | Description                                  |
|---------------|-----------|----------------------------------------------|
| fact_id       | INT (PK)  | Surrogate key                                |
| client_id     | INT (FK)  | References `client` table                    |
| contact_id    | INT (FK)  | References `contact` table                   |
| campaign_id   | INT (FK)  | References `campaign` table                  |
| subscribed    | STRING    | Subscription status (`yes` or `no`)          |

# Synthetic Features

- age_group in client table: Range of ages
- duration_length in contact table: Categorizes duration into qualitative labels.

