# GitHub Webhook Listener & MongoDB Logger

This project acts as a real-time bridge between GitHub repositories and a database. It listens for specific GitHub events (Push, Pull Request, Merge) via webhooks and automatically logs the details into MongoDB.

## 🚀 Features

* **Real-time Event Listening:** Uses Flask to expose a webhook endpoint.
* **Event Parsing:** Automatically detects and differentiates between:
    * **Push:** Logs author, branch, and timestamp.
    * **Pull Request:** Logs author, source branch, and target branch.
    * **Merge:** Detects merged PRs and logs them specifically for "Brownie Points".
* **Database Storage:** Stores all parsed events into a MongoDB collection for future retrieval.

## 🛠️ Tech Stack

* **Python 3**
* **Flask** (Web Server)
* **PyMongo** (Database Driver)
* **MongoDB Atlas** (Cloud Database)
* **ngrok** (Localhost Tunneling)

## ⚙️ Setup & Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Install Dependencies:**
    ```bash
    pip install flask pymongo
    ```

3.  **Configure MongoDB:**
    * Update the `MongoClient` connection string in `app.py` with your MongoDB Atlas credentials.

4.  **Run the Server:**
    ```bash
    python app.py
    ```

5.  **Expose Localhost (for testing):**
    ```bash
    ngrok http 5000
    ```
    * Copy the generated HTTPS URL (e.g., `https://xyz.ngrok-free.app`).

6.  **Set up GitHub Webhook:**
    * Go to your Repo Settings -> Webhooks.
    * Payload URL: `YOUR_NGROK_URL/webhookcall`
    * Content type: `application/json`
    * Select events: **Pushes** and **Pull Requests**.

## 📡 API Endpoints

* `POST /webhookcall`: The main entry point for GitHub webhooks.
