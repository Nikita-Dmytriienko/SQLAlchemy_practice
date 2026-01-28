INSERT INTO employers (username) VALUES
('Boba'),
('Roma'),
('Vitya');

select * from resumes;

select *, compensation-avg_workload_compensation as compensation_diff
from
(select
	w.id,
	w.username,
	r.compensation,
	r.workload,
	avg(r.compensation) over (partition by workload) ::int as avg_workload_compensation	
	from resumes r
	join workers w on r.worker_id = w.id) helper1

