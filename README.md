# askLAW

This project was undertaken as part of Vectara Hackthathon organised on LabLab.ai. 

Indian Legal research tools are still keyword search based. To assist lawyers better, the genAI capabilities can be used to give them the flexibility to look for answers to their questions. Lawyers also need proper citation of the cases that thay are citing.

LLM powered Retrievel augmented generation can server these twin requirement of Lawyers : Natural Language based search and Grounded Generation. 

# Data Used

We used Case data from kaggle which was primarily scrapped from indiankanoon.org. [Kaggle Dataset](https://www.kaggle.com/datasets/anudit/india-legal-cases-dataset)

# Approach

Vectara APIs were used for data injestion and querying. The raw data from kaggle was first meshed into schema needed by Vectara. It was then injested to Vectara Data Source. 

## How did we improve results?

There were cases where the query result was not directly available in a chunk provided by Vectara by default. In such cases, the problem would be solved, if summariser had more context and not just the line that was similar to the query. To solve this, the context configuration was changed. Number of sentences before and after the sentences found similar were also fed to LLM for querying.
