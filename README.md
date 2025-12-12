# BioScan Sample Analysis

This repository contains the sample analysis script for BioScan.

## Setup Instructions

### 1. Create a GitHub Repo
1.  Go to GitHub and create a new repository named `bioscan-analysis`.
2.  Push this local repository to GitHub:
    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    git branch -M main
    git remote add origin <YOUR_GITHUB_REPO_URL>
    git push -u origin main
    ```

### 2. Configure Jenkins Freestyle Job
1.  Open Jenkins and click **New Item**.
2.  Enter a name (e.g., `BioScan-Analysis`) and select **Freestyle project**. Click **OK**.
3.  **Source Code Management**:
    *   Select **Git**.
    *   Enter your Repository URL (e.g., `https://github.com/<username>/bioscan-analysis.git`).
    *   Specify the branch (e.g., `*/main`).
4.  **Build Steps**:
    *   Add a build step **Execute Shell** (or **Execute Windows batch command** if on Windows).
    *   Command: `python analyze_samples.py`
5.  **Post-build Actions**:
    *   Select **Archive the artifacts**.
    *   Files to archive: `analysis_results.csv`.
6.  Click **Save**.

### 3. Trigger the Job
1.  Click **Build Now** on the Jenkins job page.
2.  Once finished, check the **Console Output** to see the logs.
3.  Verify that `analysis_results.csv` is available in the **Build Artifacts** section.

### 4. Integrate GitHub Webhooks
1.  In your Jenkins job configuration, under **Build Triggers**, check **GitHub hook trigger for GITScm polling**. Save the job.
2.  Go to your GitHub repository **Settings** > **Webhooks**.
3.  Click **Add webhook**.
4.  **Payload URL**: `http://<your-jenkins-server>/github-webhook/`
5.  **Content type**: `application/json`.
6.  Click **Add webhook**.
7.  Now, every commit to the repository will automatically trigger the Jenkins job.
