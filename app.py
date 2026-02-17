from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///monday_clone.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-here'

db = SQLAlchemy(app)


# Database Models
class Board(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    groups = db.relationship('Group', backref='board', lazy=True, cascade='all, delete-orphan')

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    color = db.Column(db.String(20), default='#0086c0')
    board_id = db.Column(db.Integer, db.ForeignKey('board.id'), nullable=False)
    position = db.Column(db.Integer, default=0)
    items = db.relationship('Item', backref='group', lazy=True, cascade='all, delete-orphan')

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey('group.id'), nullable=False)
    status = db.Column(db.String(50), default='Not Started')
    priority = db.Column(db.String(50), default='Medium')
    assignee = db.Column(db.String(100))
    due_date = db.Column(db.Date)
    notes = db.Column(db.Text)
    position = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Create tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def index():
    boards = Board.query.order_by(Board.created_at.desc()).all()
    return render_template('index.html', boards=boards)

@app.route('/board/<int:board_id>')
def board(board_id):
    board = Board.query.get_or_404(board_id)
    groups = Group.query.filter_by(board_id=board_id).order_by(Group.position).all()
    return render_template('board.html', board=board, groups=groups)

# API Routes
@app.route('/api/boards', methods=['GET', 'POST'])
def manage_boards():
    if request.method == 'POST':
        data = request.json
        board = Board(name=data['name'], description=data.get('description', ''))
        db.session.add(board)
        db.session.commit()
        return jsonify({'id': board.id, 'name': board.name, 'description': board.description})
    
    boards = Board.query.all()
    return jsonify([{'id': b.id, 'name': b.name, 'description': b.description} for b in boards])

@app.route('/api/boards/<int:board_id>', methods=['DELETE', 'PUT'])
def update_board(board_id):
    board = Board.query.get_or_404(board_id)
    
    if request.method == 'DELETE':
        db.session.delete(board)
        db.session.commit()
        return jsonify({'success': True})
    
    if request.method == 'PUT':
        data = request.json
        board.name = data.get('name', board.name)
        board.description = data.get('description', board.description)
        db.session.commit()
        return jsonify({'id': board.id, 'name': board.name, 'description': board.description})

@app.route('/api/groups', methods=['POST'])
def create_group():
    data = request.json
    group = Group(
        name=data['name'],
        board_id=data['board_id'],
        color=data.get('color', '#0086c0')
    )
    db.session.add(group)
    db.session.commit()
    return jsonify({
        'id': group.id,
        'name': group.name,
        'color': group.color,
        'board_id': group.board_id
    })

@app.route('/api/groups/<int:group_id>', methods=['DELETE', 'PUT'])
def manage_group(group_id):
    group = Group.query.get_or_404(group_id)
    
    if request.method == 'DELETE':
        db.session.delete(group)
        db.session.commit()
        return jsonify({'success': True})
    
    if request.method == 'PUT':
        data = request.json
        group.name = data.get('name', group.name)
        group.color = data.get('color', group.color)
        db.session.commit()
        return jsonify({'id': group.id, 'name': group.name, 'color': group.color})

@app.route('/api/items', methods=['POST'])
def create_item():
    data = request.json
    item = Item(
        name=data['name'],
        group_id=data['group_id'],
        status=data.get('status', 'Not Started'),
        priority=data.get('priority', 'Medium'),
        assignee=data.get('assignee', ''),
        notes=data.get('notes', '')
    )
    
    if data.get('due_date'):
        item.due_date = datetime.strptime(data['due_date'], '%Y-%m-%d').date()
    
    db.session.add(item)
    db.session.commit()
    
    return jsonify({
        'id': item.id,
        'name': item.name,
        'status': item.status,
        'priority': item.priority,
        'assignee': item.assignee,
        'due_date': item.due_date.isoformat() if item.due_date else None,
        'notes': item.notes
    })

@app.route('/api/items/<int:item_id>', methods=['DELETE', 'PUT'])
def manage_item(item_id):
    item = Item.query.get_or_404(item_id)
    
    if request.method == 'DELETE':
        db.session.delete(item)
        db.session.commit()
        return jsonify({'success': True})
    
    if request.method == 'PUT':
        data = request.json
        item.name = data.get('name', item.name)
        item.status = data.get('status', item.status)
        item.priority = data.get('priority', item.priority)
        item.assignee = data.get('assignee', item.assignee)
        item.notes = data.get('notes', item.notes)
        
        if data.get('due_date'):
            item.due_date = datetime.strptime(data['due_date'], '%Y-%m-%d').date()
        
        db.session.commit()
        
        return jsonify({
            'id': item.id,
            'name': item.name,
            'status': item.status,
            'priority': item.priority,
            'assignee': item.assignee,
            'due_date': item.due_date.isoformat() if item.due_date else None,
            'notes': item.notes
        })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
