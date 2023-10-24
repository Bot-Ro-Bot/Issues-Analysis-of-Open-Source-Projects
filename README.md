# Issues Analysis Of Pytorch And Tensorflow For Comparing Bug Fixing Process


## 1. Introduction

A bug is an error, flaw, or fault in software code that causes it to behave unexpectedly or produce incorrect results. Debugging is the process of identifying and correcting these errors in the code. GitHub, a popular hosting service for version control systems called git, provides a tool called GitHub issues that helps manage collaborative projects and track progress. It allows you to create descriptions of tasks, bugs, changes, and updates for systematic tracking and addressing. This project explores the use of GitHub issues to analyze the bug-fixing process of two open-source machine learning frameworks: PyTorch and TensorFlow.

## 2. Development 

### 2.1 Extracting Issues from GitHub Repository
GitHub provides an API that can be used to interact with GitHub. It allows you to create and manage repositories, branches, issues, pull requests fetching publicly available data, and many more. This project utilizes the GitHub API to extract issue data from the repository of Pytorch and TensorFlow. The API, however, only gives 100 issues per page at max and it is therefore required to handle the pagination problem while fetching the issue data. For this, the issue end page was determined from the webpage of individual repositories and a simple for loop was used until the end of the issues data.

```
def handle_pagination(api_link, total_pages=100):
    data = []
    for i in tqdm(range(1, total_pages+1)):
        data.extend(get_data(api_link, i))
    return data
```

Pytorch repository has about **31503** issues as of February 15, 2023. Out of this, **21175** are closed issues and **10328** are open. When fetching data through GitHub's API, the API also gives the pull request data alongside the issues data. 

The closed issues were extracted and the pull request data was filtered out. After this, the issues closed within the last two years were selected using Pandas.

Total # of closed issues given by GitHub API (with pull request): **83769**
Total # of closed issues (without pull request data): **21175**
Total # of closed issues since last two years (>=2021-02-15): **8272**

Same processes were followed for extracting tensorflow issues data.
Total # of closed issues given by GitHub API (with pull request): **56989**
Total # of closed issues (without pull request data): **34629**
Total # of closed issues since last two years (>=2021-02-15): **8223**

Click [here](https://github.com/anishapant21/PyTen-Bug-Fix-Analysis/blob/main/data/sample.json) for sample json data.



### 2.2 Metrics

GitHub issues have various data categories that include metrics such as issue open, close and updated date, number of comments on issues, issues reopened cases, number of commits, milestones, reactions, bug density, timeline events, labels, author association, etc. 

```
['url',
 'repository_url',
 'labels_url',
 'comments_url',
 'events_url',
 'html_url',
 'id',
 'node_id',
 'number',
 'title',
 'user',
 'labels',
 'state',
 'locked',
 'assignee',
 'assignees',
 'milestone',
 'comments',
 'created_at',
 'updated_at',
 'closed_at',
 'author_association',
 'active_lock_reason',
 'body',
 'reactions',
 'timeline_url',
 'performed_via_github_app',
 'state_reason',
 'draft',
 'pull_request']
```

The following metrics have been chosen for bug fixing process analysis of the two GitHub projects (Pytorch and Tensorflow):

![image](https://user-images.githubusercontent.com/44058515/219898889-b3398f3a-337f-4de4-8edd-1d28c8076a45.png)


[PyTorch CSV dataset](https://github.com/anishapant21/PyTen-Bug-Fix-Analysis/blob/main/data/pytorch.csv) <br />
[TensorFlow CSV dataset](https://github.com/anishapant21/PyTen-Bug-Fix-Analysis/blob/main/data/tensorflow.csv)

#### 2.2.1 Mean Time to Fix (MTTF)

Time of fix, as the name implies, is the total time in days taken to fix an issue. It is calculated by subtracting the issue open date from the issue closed date. 

```MTTF (in days) = closed_date - opened_date```

The time of fix metric is highly relevant to the bug fixing process as it provides information about the timeline involved in fixing a bug, and informs about the severity of the bugs and other hidden bugs within the bug. Its analysis reveals information about the efficiency of solving a bug and could help with delayed releases, freeing up resources (developers, testers and equipment) and flawed releases.


#### 2.2.2 Issue Labels (Labels)

Labels are ways for categorizing issues, pull requests, and discussions provided by GitHub. Some of the default labels that GitHub provides are bug, documentation, duplicate, enhancement, good first issue, help wanted, invalid, question and won't fix. Any new issue will have at least one label on them. GitHub labels can help streamline the bug-fixing process by providing a clear and organized way to categorize and prioritize issues, track progress, and ensure that bugs are addressed in a timely and efficient manner.

For this analysis, the labels assigned to issues on creation are taken into consideration. The labels data category from GitHub can have a list of multiple labels within them, from which the label assigned on creation (the first label on the list) is extracted using the "name" key from the dataset.

```
"labels": [
            {
                "id": 284443156,
                "node_id": "MDU6TGFiZWwyODQ0NDMxNTY=",
                "url": "https://api.github.com/repos/tensorflow/tensorflow/labels/type:docs-bug",
                "name": "type:docs-bug",
                "color": "159b2e",
                "default": false,
                "description": "Document issues"
            }
        ]
```

#### 2.2.3 Number of Issue Comments (Comments)

The number of issue comments in GitHub can be an indicator of the level of activity, priority and progress in the bug-fixing process. A large number of personal interests (large star count  or lots of comments) in a bug is an indication of bug popularity and may impact bug ﬁxing time. **[[4](https://github.com/anishapant21/PyTen-Bug-Fix-Analysis/edit/main/README.md#5-references)]** has found that bugs having less than four comments (less discussion) get ﬁxed faster as compared to other bugs. 

#### 2.2.4 Author Association (AuthorA)

Author association on GitHub describes the connection between a user who submitted an issue and their level of involvement with the repository where the issue was submitted. The authors of the issues extracted from Pytorch and Tensorflow are Collaborators, contributors, members, and none. <br/>
MEMBER: The user is a member of the organization that owns the repository <br/>
CONTRIBUTOR: The user has contributed to the repository by opening an issue, creating a pull request, or commenting on an issue or pull request. <br/>
COLLABORATOR: The user has been given push access to the repository. <br/>
NONE: The user has no association with the repository. <br/>

The author associated with an issue in GitHub can play a role in determining the priority of issue fixing. Issues created by COLLABORATORs, MEMBERs, or OWNERs of a repository may be given higher priority because these users are typically more closely involved with the project and may have a better understanding of its overall goals and priorities.


#### 2.2.5 Number of Positive Reactions (Reactions)

The number of positive reactions (such as "thumbs up" or "heart" reactions) on GitHub issues can be a useful way to gauge the level of interest, engagement, and feedback from users, which can help guide developers in their efforts to fix bugs. **[[3](https://github.com/anishapant21/PyTen-Bug-Fix-Analysis/edit/main/README.md#5-references)]** research showed that bugs and enhancements with at least two reactions take more time to be closely compared to the ones without reactions. They hypothesize that they are more complex and require more time from developers to be resolved.

In highlighting the importance of positive reactions in the bug-fixing process, the positive reaction (having a key value of "+1") is extracted from the reaction category of the dataset.

```
"reactions": {
            "url": "https://api.github.com/repos/tensorflow/tensorflow/issues/5/reactions",
            "total_count": 98,
            "+1": 88,
            "-1": 0,
            "laugh": 0,
            "hooray": 10,
            "confused": 0,
            "heart": 0,
            "rocket": 0,
            "eyes": 0
        }
```

## 3. Findings

### 3.1 Exploratory Analysis (Data)

| Comparison Parameters(Last two years 2021-2023) | TensorFlow   | PyTorch                |
|-------------------------------------------------|--------------|------------------------|
| Total Number of Issues Closed                   | 8223         | 8272                   |
| Average Fix time per issue                      | 296 days     | 155 days               |
| Average Comments Per Issue                      | 7.61         | 3.88                   |
| Average Reaction Per Issue                      | 0.54         | 0.45                   |
| Total Comments                                  | 62597        | 32136                  |
| Total Reactions                                 | 4482         | 3754                   |
| Author Association for Least Number of Issues   | Collaborator | Member                 |
| Author Association for Most Number of Issues   | None*        | None*                 |
| Most used labels                                | high priority      | stat:awaiting response |

*: None implies independent github user

### 3.2 Exploratory Analysis (Graph)

#### 3.2.1 Comparison Through MTTF of the Issues 

PyTorch             |  TensorFlow
:-------------------------:|:-------------------------:
![image](https://github.com/anishapant21/PyTen-Bug-Fix-Analysis/blob/main/figure/data_distribution_MTTF_pt.png)  |  ![image](https://github.com/anishapant21/PyTen-Bug-Fix-Analysis/blob/main/figure/data_distribution_MTTF_tf.png)

![image](https://github.com/anishapant21/PyTen-Bug-Fix-Analysis/blob/main/figure/sample_distribution_MTTF_both.png)

A graphical analysis of the distribution of the mean time to fix the issues of both the PyTorch and TensorFlow repositories shows that most of the issues were closed below the 200 days mark. The number of issues opened between the 250 and 1000 days was marginally higher for TensorFlow in comparison to PyTorch. Similarly, from the normal distribution graph of the data, it can be inferred that only 0.3% of issues took more than 1500 days to be fixed for both projects.

PyTorch             |  TensorFlow
:-------------------------:|:-------------------------:
![image](https://github.com/anishapant21/PyTen-Bug-Fix-Analysis/blob/main/figure/MTTF_closed_pytorch.png)  |  ![image](https://github.com/anishapant21/PyTen-Bug-Fix-Analysis/blob/main/figure/MTTF_closed_tensorflow.png)


Another graphical analysis done was that of the trend of the issue closing trend. For this, the cumulated issues over time were plotted against the closing date of the issues. At the beginning of 2021, the number of issues solved was higher for TensorFlow than PyTorch. But over time, PyTorch had a steep rise in the bugs reported while TensorFlow had a steady rise in the number of bugs, thus resulting in almost the same number of bugs at the beginning of 2023.  Furthermore, both projects have a smooth curve implying that the bug-fixing process is continuous for both projects.

PyTorch             |  TensorFlow
:-------------------------:|:-------------------------:
![image](https://github.com/anishapant21/PyTen-Bug-Fix-Analysis/blob/main/figure/MTTF_created_pytorch.png)  |  ![image](https://github.com/anishapant21/PyTen-Bug-Fix-Analysis/blob/main/figure/MTTF_created_tensorflow.png)

The graph of Mean Time to Fix (MTTF) against the issue open date was also plotted to analyze the efficiency of the bug-fixing process. The above scatter plots clearly show that both the PyTorch and the TensorFlow projects have backlogs of unresolved issues ( and finally solved within the last two years), dating back to 2017 and 2016 respectively. The MTTF value for issues opened within the last two years is less than previous issues (recent issues are fixed in lesser time than previous issues) and shows a continuously improving efficiency over the years. This is true for both projects.


#### 3.2.2 Comparison Through Author Association Distribution

![image](https://github.com/anishapant21/PyTen-Bug-Fix-Analysis/blob/main/figure/disrt_AA_pt.png)

Most of the issues originate from independent GitHub users for both TensorFlow and PyTorch. The least number of issues reported on GitHub for PyTorch is associated with Member users, and for TensorFlow is Collaborator. 

Average value for MTTF for NONE: **153 Days**  <br/>
Average value for MTTF for CONTRIBUTOR: **164 Days**
 <br/>
Average value for MTTF for COLLABORATOR: **136 Days** <br/>
Average value for MTTF for MEMBER: **140 Days**  <br/>

Similarly, for TensorFlow, <br/>
Average value for MTTF for NONE: **275 Days** <br/>
Average value for MTTF for CONTRIBUTOR: **455 Days** <br/>
Average value for MTTF for COLLABORATOR: **390 Days** <br/>
Average value for MTTF for MEMBER: **410 Days** <br/>

It can be inferred from the data that issues originated from Member and  collaborator are given high precedence in both the projects and therefore have a shorter time to fix.


#### 3.2.3 Comparison Through Issues Labels


PyTorch             |  TensorFlow
:-------------------------:|:-------------------------:
![image](https://github.com/anishapant21/PyTen-Bug-Fix-Analysis/blob/main/figure/dist_gra_labels_pt.png)  |  ![image](https://github.com/anishapant21/PyTen-Bug-Fix-Analysis/blob/main/figure/dist_gra_labels_tf.png)

 The bar plot of labels of the issues reveals that PyTorch encountered and resolved 10 severity bugs in the system. The severity of the bugs directly correlates with the time of fixing the bug: the higher the severity, the more time is required for the bug to be fixed. It may be because of the intensity of the testing involved in the process. PyTorch uses a label called “high priority” to indicate the priority of the issues. In the case of TensorFlow, however, the higher the severity the lesser the time required to solve them. It implies that TensorFlow is more efficient with its high-severity bug fixes than PyTorch.

#### 3.2.4 Comparison Through Number of Comments and Number of Positive Reactions on the Issues


Comments             | Positive Reactions
:-------------------------:|:-------------------------:
![image](https://github.com/anishapant21/PyTen-Bug-Fix-Analysis/blob/main/figure/density_comments.png)  |  ![image](https://github.com/anishapant21/PyTen-Bug-Fix-Analysis/blob/main/figure/density_reactions.png)

PyTorch             |  TensorFlow
:-------------------------:|:-------------------------:
![image](https://github.com/anishapant21/PyTen-Bug-Fix-Analysis/blob/main/figure/comm_pt.png)  |  ![image](https://github.com/anishapant21/PyTen-Bug-Fix-Analysis/blob/main/figure/comm_tf.png)

PyTorch             |  TensorFlow
:-------------------------:|:-------------------------:
![image](https://github.com/anishapant21/PyTen-Bug-Fix-Analysis/blob/main/figure/react_pt.png)  |  ![image](https://github.com/anishapant21/PyTen-Bug-Fix-Analysis/blob/main/figure/react_tf.png)

A graph of MTTF Vs. Number of Comments shows that, for both projects, as the number of comments increases on a particular issue, the time taken to fix that issue significantly decreases. It may be due to the fact that a more popular issue, assessed by the number of comments,  gets more exposure by developers and signifies precedence of the issue. The graph of MTTF Vs. Positive Reactions also corroborate this trend. However, it should be noted that more comments (or reactions) don't always mean the issue is important or will have a shorter fix time. Many issues with a number of comments less than 20 also have a lower fix time.



## 4. How to run your code
```
virtualenv env
pip3 install -r requirements.txt 
jupyter-notebook PyTen_Data_Extraction.ipynb
jupyter-notebook PyTen_Data_Analysis.ipynb
```

## 5. REFERENCES

1. https://www.linkedin.com/pulse/time-fix-defects-ivan-luizio-magalh%C3%A3es
2. Empirical Analysis of the Bug Fixing Process in Open Source Projects
3. Beyond Textual Issues: Understanding the Usage and Impact of GitHub Reactions
4. Comparison of Seven Bug Report Types: A Case-study of Google Chrome Browser Project
5. An Empirical Study on Bugs inside TensorFlow
6. Predicting eclipse bug lifetimes
7. Performance Assessment of Bug Fixing Process in Open Source

