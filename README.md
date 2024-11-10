# Project Name: Assignment_SD1

## Description
Assignment_SD2 is a version-controlled project designed for a simulated development team to practice version control with Git. Each team member fulfills a specialized role to manage, develop, test, and release a product, with rigorous version control and collaboration requirements.

## Project Structure
The project follows a structured Git workflow that includes:
- *Master Branch*: Managed by the Lead Integrator, containing stable releases.
- *Develop Branch*: Overseen by the Development Integrator for integrating new features and hotfixes.
- *Feature Branches*: Separate branches for implementing features 1, 2, and optional feature 3.
- *Hotfix Branches*: Created as needed to address critical bugs.

## Git Workflow
This project uses a staged workflow that simulates a complete software development lifecycle, with each step contributing to the final stable product.

### Project Steps

1. *Initialization*: 
   - The project starts by creating the master branch, where a basic README file and initial documentation are added. The develop branch is also created at this stage, setting up a workspace for active development separate from the main stable version in master.

2. *Feature Development*:
   - Each feature is developed in its dedicated branch (feature1, feature2, etc.). This keeps each feature isolated to ensure that work on one part of the project does not interfere with others. Feature developers implement, test, and refine their code within these branches, simulating real-world feature development where multiple features might be under construction simultaneously.

3. *Integration into Develop*:
   - Once a feature is complete, it is merged into the develop branch. This branch acts as a testing ground where all features are combined. Any conflicts between features are resolved here, and additional testing is conducted to make sure the integrated features work harmoniously.

4. *Preparing for Release*:
   - When a stable version is ready, a release branch (e.g., release1) is created from develop. This branch allows final adjustments and bug fixes without interrupting ongoing development work in develop. The release branch is carefully tested and prepared for deployment as a stable version.

5. *First Release (v1.00)*:
   - After the final testing and adjustments in the release branch, it is merged into master, marking the official release of version v1.00. A version tag is applied to keep a record of this release for future reference.

6. *Critical Bug Fixing (Hotfix)*:
   - If critical bugs are identified in the release, a hotfix branch (e.g., hotfix1) is created from master. The team addresses urgent issues here and then merges the hotfix back into both master (for immediate deployment) and develop (to keep development up-to-date). This step is essential for maintaining a stable and reliable product in production.

7. *Ongoing Development and Additional Releases*:
   - Development continues with the addition of new features ( feature3) and improvements. These are handled in separate branches and integrated into develop, following the same process. Once these are stable, they can be merged into master as additional releases, each tagged with a new version (v1.02).

8. **Ongoing Development and Additional Releases (continued)**:
   - Development continues with the addition of new features (feature3) and improvements. These are handled in separate branches and integrated into the develop branch, following the same process. Once these are stable, they can be merged into master as additional releases, each tagged with a new version (e.g., v1.02).

9. **Feature 2 Final Development (F2)**:
   - **Feature 2 Completed**: The final development phase for feature2 is completed. After resolving any issues, the branch undergoes a **rebase** with the develop branch to ensure that feature2 is up-to-date with the latest changes from the develop branch.
   - **Rebase**: Developers will rebase feature2 onto the latest develop to incorporate any updates or bug fixes that were made to the develop branch in parallel to feature2 development.

10. **Feature 3 Implementation (X)**:
    - **New Feature in Development**: Feature3 development begins in its own branch. This feature could require additional challenges or changes, making it a more complex development effort. 
    - Developers will work on feature3 independently, making sure to follow the same process of testing, updating, and ensuring compatibility with the ongoing codebase in develop.

11. **Merge of Feature 3 into Develop (Y)**:
    - **Merge to Develop**: Once feature3 is complete and tested, it is merged into the develop branch. Any conflicts that arise during this merge will be resolved to ensure smooth integration of feature3 into the development code.
    - At this point, feature3 should be fully integrated into the develop branch and ready for further testing.

12. **Merge Develop into Master (Z)**:
    - **Merge of Develop into Master**: Once develop is fully stable and contains all the necessary features, including the latest feature3, it is merged into master. This marks the final step before the release of the next version of the software.
   
13. **Adding Tests and Final Structure(Z1)**

  - Incorporating Tests into the Codebase: For better understanding of the code and to ensure its reliability, tests that have been used throughout the development process (including during feature1, feature2,       and feature3) are now added. These tests are incorporated into each of the features folders.
  - A version tag (e.g., `v1.02`) is applied to this commit to mark the official release version, signifying that the software is stable and ready for deployment.
### Key Branches and Tags
- *master*: Houses stable releases, with each release tagged for easy reference.
- *develop*: Combines completed features and hotfixes for testing and integration.
- *feature1, **feature2, **feature3*: Isolated branches for specific features.
- *hotfix1*: Branch for addressing critical bugs post-release.

### Features


- **Feature 1**: Handles data cleaning by removing columns with NaN values and splits the data into features and labels for classification.
- **Feature 2**: Implements Principal Component Analysis (PCA) to reduce the dimensionality of the dataset, improving model performance and computation.
- **Feature 3**: Focuses on data analysis and visualization, providing insights through statistical methods and graphical representations
- *Hotfixes*: Applied when critical issues are found in released versions.

## Roles
Each member of the team fulfills a specific role to mimic a real development environment:
- *Lead Integrator*: Manages the master branch and oversees tagging for stable releases.
- *Development Integrator*: Ensures quality in develop by overseeing integration.
- *Feature Developers*: Implement features in dedicated branches, simulating a collaborative environment.
- *Maintenance and Hotfix Manager*: Manages bug fixes and critical patches.
- *QA and Final Verification*: Conducts testing and ensures all elements are properly integrated before a release.

## Getting Started

### Prerequisites
- pandas==1.5.3
- numpy==1.23.5
- scikit-learn==1.1.3
- matplotlib==3.6.2
- seaborn==0.12.1

### Installation
1. 1. **Set up Git**:
   - Clone the repository:
     ```bash
     git clone <https://github.com/rayen003/repo/>
     ```
