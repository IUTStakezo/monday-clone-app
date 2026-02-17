# Monday Clone - Project Management Application

A feature-rich project management application inspired by Monday.com, built with Python Flask and SQLite.

## Features

✅ **Board Management**
- Create, edit, and delete project boards
- Organize multiple projects in one place
- Add descriptions to boards

✅ **Group Organization**
- Create groups within boards to categorize tasks
- Customize group colors for visual organization
- Flexible grouping structure

✅ **Task Management**
- Add items (tasks) to groups
- Track status: Not Started, Working on it, Stuck, Done
- Set priority levels: Low, Medium, High
- Assign tasks to team members
- Set due dates
- Add detailed notes to tasks

✅ **Modern UI**
- Clean, professional interface
- Color-coded status and priority badges
- Responsive design
- Modal-based editing
- Smooth animations

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation & Setup

### 1. Extract the Files
Unzip the downloaded file to your desired location.

### 2. Navigate to the Project Directory
```bash
cd monday-clone-app
```

### 3. Create a Virtual Environment (Recommended)
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

## Running the Application

### Start the Server
```bash
python app.py
```

### Access the Application
Open your web browser and navigate to:
```
http://localhost:5000
```

The application will automatically create the database on first run.

## Usage Guide

### Creating Your First Board
1. Click the "New Board" button on the home page
2. Enter a board name (e.g., "Marketing Campaign")
3. Optionally add a description
4. Click "Save Board"

### Adding Groups to Your Board
1. Open a board by clicking on it
2. Click "Add Group" button
3. Enter a group name (e.g., "In Progress", "To Do")
4. Choose a color for visual organization
5. Click "Save Group"

### Creating Tasks (Items)
1. Inside a group, click "Add Item"
2. Fill in the task details:
   - **Name**: What needs to be done
   - **Status**: Current state (Not Started, Working, Stuck, Done)
   - **Priority**: Importance level (Low, Medium, High)
   - **Assignee**: Who's responsible
   - **Due Date**: When it's due
   - **Notes**: Additional details
3. Click "Save Item"

### Editing and Deleting
- Click "Edit" buttons to modify boards, groups, or items
- Click "Delete" to remove (confirmation required)

## Project Structure

```
monday-clone-app/
│
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── README.md              # This file
│
├── templates/             # HTML templates
│   ├── base.html         # Base template with common layout
│   ├── index.html        # Boards listing page
│   └── board.html        # Board detail view with groups/items
│
└── monday_clone.db       # SQLite database (created on first run)
```

## Database Schema

### Boards
- id, name, description, created_at

### Groups
- id, name, color, board_id, position

### Items (Tasks)
- id, name, group_id, status, priority, assignee, due_date, notes, position, created_at

## Customization

### Changing the Port
Edit `app.py` and modify the last line:
```python
app.run(debug=True, port=5000)  # Change 5000 to your desired port
```

### Adding New Statuses or Priorities
Edit the `<select>` options in `templates/board.html`:
```html
<select id="itemStatus">
    <option value="Not Started">Not Started</option>
    <option value="Your New Status">Your New Status</option>
</select>
```

Then add corresponding CSS classes in the style section:
```css
.status-your-new-status {
    background-color: #yourcolor;
    color: white;
}
```

## Troubleshooting

### Port Already in Use
If you see "Address already in use", either:
- Stop the other application using port 5000
- Change the port in `app.py`

### Database Errors
Delete `monday_clone.db` and restart the application to create a fresh database.

### Module Not Found Errors
Make sure you've activated the virtual environment and installed dependencies:
```bash
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Development Tips

### Using with VS Code
1. Install the Python extension
2. Open the project folder in VS Code
3. Select the Python interpreter from your virtual environment
4. Use the built-in terminal to run commands

### Using with GitHub Copilot
1. Sign up for a GitHub account (free)
2. Enable GitHub Copilot in VS Code
3. Start typing and Copilot will suggest completions
4. Press Tab to accept suggestions

## Future Enhancements

Potential features to add:
- User authentication and login
- Team collaboration features
- File attachments
- Activity timeline
- Email notifications
- Kanban board view
- Calendar view
- Search and filters
- Data export (CSV, Excel)
- Dark mode

## Technical Stack

- **Backend**: Python Flask
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **UI Design**: Custom CSS (Monday.com inspired)

## License

This is a learning project. Feel free to use and modify as needed.

## Support

If you encounter issues:
1. Check the Troubleshooting section
2. Review the error messages in the terminal
3. Ask Claude AI for help with specific error messages
4. Use GitHub Copilot in VS Code for code assistance

## Version

Version 1.0.0 - Initial Release

---

**Happy Project Managing! 📋✨**
