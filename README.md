# Lead Optimization & Profit Maximization Tool

## Project Overview

The **Lead Optimization & Profit Maximization Tool** is an advanced solution designed to maximize profits while intelligently allocating marketing resources. By combining **machine learning, clustering, and Monte Carlo simulations**, this tool enables data-driven decisions about lead acquisition costs, ensuring the highest possible return on investment.  

The core idea is to **cluster leads based on their similarities** and then optimize the **cost of acquisition per cluster**, rather than individually per lead. This approach is both **resource-efficient** and **legally safer** compared to individual-level cost optimization.

> **Note:** Within this tool, the terms **“Cost”** and **“Expense”** are used interchangeably.

The application is **deployed online** and can be accessed here: [Lead Optimizer App](https://ktbridge-lead-optimizer-app-dmaipu.streamlit.app/)

---

## Machine Learning Models

A diverse set of **supervised machine learning models** were trained to predict lead conversion (`1`) vs non-conversion (`0`) and to identify the models most **sensitive to the cost feature**. These models include:

- **Gaussian Naive Bayes (GNB)**
- **K-Nearest Neighbors (KNN)**
- **Support Vector Machines (SVM)**  
  - Linear  
  - Polynomial  
  - RBF  
  - Sigmoid
- **Logistic Regression**
- **Linear Discriminant Analysis (LDA)**
- **Decision Tree**
- **XGBoost**
- **Random Forest**

The purpose of training multiple models is to ensure the **robustness of predictions** and identify the model that best captures the relationship between **cost** and **lead acquisition**, which is critical for optimizing marketing spend.

---

## Clustering

To identify groups of similar leads, the tool employs **Agglomerative Clustering**, a hierarchical clustering technique that:  

- Groups leads based on feature similarity.  
- Preserves hierarchical relationships, enabling multi-level insights into lead behavior.  
- Facilitates cluster-level optimization, ensuring **profit-maximizing acquisition strategies** without targeting individual leads directly.

---

## Monte Carlo Optimization

Once clusters are established:

1. The model predicts lead conversion probabilities for each lead in a cluster.  
2. **Monte Carlo simulations** explore a range of acquisition costs for each cluster.  
3. The tool identifies the **cost that maximizes expected profit** per cluster, rather than simply choosing the minimum cost.  

This approach allows for a **highly efficient, legally compliant, and scalable optimization workflow**.

---

## Sidebar Visualizations

The sidebar provides **rich insights per cluster/bucket**:

1. **Contact Frequency Distribution**  
   - Shows how many times leads in each bucket were contacted.  
   - Visualized as **horizontal bar charts** highlighting **25th, 50th, and 75th percentiles**.

2. **Days to Respond Distribution**  
   - Displays response times per lead using **boxplots**, highlighting medians, quartiles, and outliers.

3. **Total Campaign Cost (Pre-Clustering)**  
   - Horizontal bar chart showing **min, 25th, 50th, 75th, and max values**.  
   - Provides a snapshot of potential spending **before optimization**, helping visualize baseline expenses.

4. **Gauge Chart (Pre-Clustering)**  
   - Illustrates the **mean cost per cluster** relative to the median.  
   - Highlights clusters where spending is skewed, helping decision-makers identify **unusually high or low cost clusters** and guide strategic allocation.

---

## Optimization Insights

- Cluster-level optimization allows you to **maximize profit per group** rather than per lead.  
- The tool identifies **cost ranges that yield the highest profit**, avoiding trivial solutions where the lowest cost is always selected.  
- By combining ML predictions, clustering, and Monte Carlo simulations, it provides a **practical and actionable strategy** for lead acquisition.

---

## How to Use

You can use the provided data_to_test_on.csv file to see how the tool works on a sample dataset.

On any other dataset with a similar structure, the tool can be applied directly — simply load your own leads file, and the same workflow of clustering, ML prediction, Monte Carlo simulation, and profit optimization will function seamlessly.

This ensures that the tool is flexible and adaptable to different lead databases, campaign types, or business scenarios.

---

### Notes

- The workflow is **cluster-focused**, ensuring computational efficiency and legal compliance.  
- Visualizations provide both **pre-optimization insights** and **cluster-level metrics** for informed decision-making.  
- Supports multiple ML models to ensure **robust predictions** and sensitivity to **cost-related features**.
