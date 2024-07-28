-- 테이블 생성
CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    position VARCHAR(100)
);

-- 데이터 삽입
INSERT INTO employees (id, name, position) VALUES (1, 'John Doe', 'Engineer');

-- 데이터 조회
SELECT * FROM employees;