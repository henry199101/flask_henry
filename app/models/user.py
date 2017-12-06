class Follow(db.Model):
	__tablename__ = 'follow'
	follower_id = db.Column(db.Integer, db.ForeignKey('users.id'),
							primary_key=True)
	followed_id = db.Column(db.Integer, db.ForeignKey('users.id'),
							primary_key=True)
	timestamp = db.Column(db.Datetime, default=datetime.utcnow)


class User(UserMixin, db.Model):
	followed = db.relation('Follow',
						   foreign_keys=[Follow.follower_id],
						   backref=db.backref('follower', lazy='joined'),
						   lazy='dynamic',
						   cascade='all, delete-orphan')
	followers = db.relation('Follow',
							foreign_keys=[Follow.followed_id],
							backref=db.backref('followed', lazy='joined'),
							lazy='dynamic',
							cascade='all, delete-orphan')