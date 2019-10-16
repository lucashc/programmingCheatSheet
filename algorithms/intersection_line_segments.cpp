# Intersection of line segments
## \note Line segments are given by the coordinates of their end points.
struct Point {

	long long x, y;

};

struct Line {
	Point p, q;
};

int sgn(long long x) {
	return x == 0 ? 0 : (x < 0 ? -1 : 1);
}

long long det(long long x1, long long y1, long long x2, long long y2) {
	return x1 * y2 - x2 * y1;
}

int orientation(Point p, Point q, Point r) {
	return sgn(det(p.x - r.x, p.y - r.y, q.x - r.x, q.y - r.y));
}

bool intersect(Line l1, Line l2) {
	if (max(l1.p.x, l1.q.x) < min(l2.p.x, l2.q.x)) return false;
	if (max(l2.p.x, l2.q.x) < min(l1.p.x, l1.q.x)) return false;
	if (max(l1.p.y, l1.q.y) < min(l2.p.y, l2.q.y)) return false;
	if (max(l2.p.y, l2.q.y) < min(l1.p.y, l1.q.y)) return false;
	return orientation(l1.q, l2.p, l1.p) * orientation(l1.q, l2.q, l1.p) <= 0
		&& orientation(l2.q, l1.p, l2.p) * orientation(l2.q, l1.q, l2.p) <= 0;
}
