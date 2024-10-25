# CS-340

How do you write programs that are maintainable, readable, and adaptable?

I focused on clear structure and simplicity. I used descriptive variable names and wrote modular code, ensuring each method had a single responsibility. This helps future developers understand and modify the program without breaking functionality. The module follows object-oriented principles, making it easy to extend or modify without rewriting the entire codebase. I included in-line comments to explain each section, and exception handling ensures the program can handle unexpected issues without crashing. Using MongoDB for database operations and implementing this module made it adaptable to changes in data structure or future database integrations.

The advantages of this approach were clear when I connected the module to the dashboard in Project Two. I could reuse the CRUD operations for database interaction without writing new code for each database operation. This saved time and made debugging easier since the CRUD operations were already tested. In the future, this CRUD module could be adapted to work with other types of databases or to support more advanced queries, extending its use to other applications that require data management. Even with the problems I had, like troubleshooting database connections or managing data flow, everything was possible because I focused on understanding the root cause and applying the right solutions.

How do you approach a problem as a computer scientist?

I first define the requirements and break the problem down into smaller, manageable parts. For example, with the database and dashboard for Grazioso Salvare, I started by identifying the key CRUD operations needed to manage animal data. I then ensured that the database schema was optimized for these operations by creating appropriate indexes and using a well-structured JSON format. This was different from previous projects because I had to integrate both back-end (MongoDB) and front-end (Dash) components while ensuring that the two systems communicated seamlessly.

Even when I faced issues such as aligning database queries with dashboard widgets, I approached the challenge step by step, solving each piece before moving on. This ensured I didn’t feel overwhelmed by the project’s scope. Moving forward, I would use similar techniques—starting with thorough requirement gathering and planning, followed by building modular, reusable components. For future client requests, I would ensure the database design is flexible enough to accommodate changes without requiring major rewrites. This approach saves time and effort in long-term maintenance and adaptability to new requirements.

What do computer scientists do, and why does it matter?

Computer scientists solve complex problems through the design and development of efficient systems and applications. My work on the CRUD Python module helped Grazioso Salvare streamline the management of their animal data, making it easier to identify and train animals for rescue operations. This type of project matters because it improves organizational efficiency, saves time, and ensures data integrity.

For a company like Grazioso Salvare, having a reliable and scalable system in place helps them focus on their core mission—training animals for rescue missions—without worrying about the technical details. Even when I faced technical challenges or issues integrating different components, I was able to make everything work through persistence and problem-solving. This not only helped the company do their work better but also made the system adaptable for future needs.
