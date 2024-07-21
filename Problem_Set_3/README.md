# Problem Set 3

Please answer the below questions:

A. Write and share a small note about your choice of system to schedule periodic tasks (such as downloading a list of ISINs every 24 hours). Why did you choose it? Is it reliable enough; Or will it scale? If not, what are the problems with it? And, what else would you recommend to fix this problem at scale in production?

B. In what circumstances would you use Flask instead of Django and vice versa? 


## Answers

A. The System to schedule periodic tasks differs from system to system as windows use "Windows Task Scheduler", Unix use "Corn" for the scheduling task. When it come to a project that is deployed in Python (Django or Flask) Celery is the best choice among most of the developers.It is beacuse asynchronous task queue is based on distributed message passing and focused on real-time operation but also supports scheduling. It is also useful for handling time-consuming operations, periodic tasks, and background processing in web applications. This Celery can be intergrated with Django as django-celery-beat and in Flask it can be directly accessed by Flask-Celery.

I choose Celery based on these reason:
- **Flexibility**: It supports various message brokers and result backends
- **Powerful**: It handles complex task scheduling and execution efficiently.
- **Reliability**: It includes features for task retries, error handling, and monitoring, which enhance the background task processing.
- **Asynchronous**: It handles time-consuming tasks asynchronously, improving application responsiveness
- **Community Support**: It is well-maintained with a large and active community.

It is designed with reliability in mind as it offers features like task retries, error handling, and persistent task queues. When properly configured, it can handle network issues, worker failures, and other common problems. However, like any system, its reliability depends on proper setup and maintenance

It is highly scalable. It can distribute tasks across multiple workers and machines, allowing it to handle increasing workloads. Its support for various message brokers also aids in building scalable architectures.

It is generally reliable and scalable as most of the  issues can arise from improper configuration, broker limitations, task design inefficiencies, inadequate error handling, or challenges in monitoring and debugging distributed tasks in complex deployments.

To reduce the problems in production at scale, I recommend to use a monitoring system to track the process and view error, use message brokers to get the regular update of the Celery in production, use circuit breakers for task failures, and considering alternative task queue systems.


B. Flask is great for small projects like microservices and APIs. It's perfect when you want to pick and choose exactly what parts to use in your project. This makes Flask lightweight and easy to mix with different technologies. However, Django is better for bigger projects that need lots of features built-in. It's really good for things like user logins, managing website content, and working with lots of data. Django comes with many tools already included, and there are tons of extra packages you can add easily. It's like getting a full toolbox instead of building your own set of tools.