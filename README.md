## Introduction
Our project ‘Kyusei’ takes the popular static analysis tool Metabob API and makes it a more personalized tool for upcoming python developers and data science enthusiasts. Static analysis is used for software development and quality assurance teams to check for vulnerabilities. What we aim to promote through our project is the mindset that even young developers or non-professionals can go through their repo's and do debugging/error analysis using automated tools.
Not only will this help the developers, but it will help in popularizing the metabob API among the developing community. The next generation of python developers should be aware of such tools which expose security vulnerabilities and other common errors in
their personal as well as professional endeavors, not to mention automated static analysis tools, are the future of debugging and a tool all developers should be familiar with.

## What it does?

The idea utilizes the concept of Pattern recognition and Contextual word embeddings along with statistical tools to aggregate and cluster problems and similar issues found in the user's/companies repositories. For this implementation, we incorporated word embeddings to find contextually similar issues. Multiple word embedding techniques like TF-IDF and bag of words and pre-trained word embedding were analyzed. However, due to the unique nature of the data distribution provided we utilized Bag-of-Words for the use case.

## How was it made?

Classic machine learning tools have provided methods to measure contextual similarity between two given sentences. We saw this opportunity in the issues, and explanations provided by Metabob API. We used the problems results of the repository analysis to generate Bag-of-Words embeddings, which would then allow us to express them numerically. The NumPy library was used for computing matrix operations, for Bag-of-Words and distance matrix computation. We refined and developed a novel implementation for plotting clustered entities, allowing us to better beautify the project. This visualization presents an easy-to-understand pictographic representation of these embeddings. Matplotlib was used as the backdrop for visualization. 
Sticking with the theme of the hack, we went for an interstellar theme centering around clusters and galaxies. The final product displayed on the web page is a cluster of repos rotating around a super-galaxy. This was done to make our product visually appealing. We used Streamlit for creating our site. Streamlit is one of the few untapped tools for Python enthusiasts that allows one to quickly build highly interactive web applications around their data, machine learning models, and pretty much anything. 


## Challenges we ran into ?
We couldn’t use the Metabob API to its fullest potential due to the limitation on repositories. We believe that having access to the public repositories of an individual’s account would allow more personalized pattern recognition. This would allow them to alleviate said issues, easily. At the same time, clusters would allow them to realize key issues which can be found in multiple repositories.
Our project aims to be a source of learning, where individuals can track and analyze their progress on issues while also giving them an opportunity to learn from the mistakes highlighted.

## What is next for Kyusei?
We believe better word embedding techniques on larger repositories would allow better clustering. This would improve the results of the current model. Finally, we believe an optional selection of the target variables which tune these embeddings would be a great addition, allowing users to customize our project.
