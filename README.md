# Lead Optimization & Profit Maximization Tool

## Project Overview

The Lead Optimization & Profit Maximization Tool is a strategic machine learning system designed to solve one of the most critical challenges in marketing and lead acquisition: how to allocate budget (or cost per lead) in a way that maximizes total profit, not just the number of leads acquired.

Rather than treating every lead equally or guessing acquisition costs, this tool uses data-driven intelligence to determine the optimal cost of acquisition for different types of leads that are grouped into clusters based on shared characteristics such as behavior patterns, engagement level, or historical conversion likelihood.

The Problem It Solves

Organizations often waste marketing spend by:

Paying too much for low-value leads

Missing out on high-value leads due to underinvestment

Applying a “one-size-fits-all” cost strategy

Making decisions based on gut feeling instead of predictive analytics

What the Project Aims to Achieve

This tool optimizes profit, not just conversion rates. Its goal is to:

Identify distinct lead segments (clusters) that behave differently in terms of conversion probability and potential revenue.

Simulate various acquisition cost strategies to predict how changes in spend will affect conversions and profitability.

Recommend the optimal acquisition cost for each cluster that maximizes net profit, taking into account diminishing returns and cost–conversion elasticity.

Ensure compliance and fairness by optimizing at the group level rather than the individual level, avoiding legal and ethical issues related to individual price discrimination.

Key Outcomes

Higher total profit by precisely balancing cost vs. expected return.

Efficient budget allocation with maximum ROI per dollar spent.

Strategic decision-making powered by machine learning, clustering, and Monte Carlo simulations.

Scalable and automated solution that can be applied to any marketing or lead-based acquisition model.

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
