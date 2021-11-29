CREATE TABLE companies (
    company_id SERIAL PRIMARY KEY  ,
	company_name VARCHAR(20)
);

CREATE TABLE video_games(
    video_game_id SERIAL PRIMARY KEY ,
    video_game_name VARCHAR(40),
	video_game_platform VARCHAR(20),
	video_game_genre VARCHAR(30),
	year_of_publication INT,
	company_id INT REFERENCES companies(company_id),
	na_sales_id INT, 
	eu_sales_id INT,
	jp_sales_id INT, 
	other_sales_id INT 
);

CREATE TABLE na_sales(
	NA_sales_id SERIAL PRIMARY KEY ,
	NA_sales FLOAT,
	sales_date DATE,
	video_game_id INT REFERENCES video_games(video_game_id)
);

CREATE TABLE eu_sales(
	EU_sales_id SERIAL PRIMARY KEY ,
	EU_sales FLOAT,
	sales_date DATE,
	video_game_id INT REFERENCES video_games(video_game_id)
);

CREATE TABLE jp_sales(
	JP_sales_id SERIAL PRIMARY KEY ,
	JP_sales FLOAT,
	sales_date DATE,
	video_game_id INT REFERENCES video_games(video_game_id)
);

CREATE TABLE other_sales(
	other_sales_id SERIAL PRIMARY KEY ,
	other_sales FLOAT,
	sales_date DATE,
	video_game_id INT REFERENCES video_games(video_game_id)
);

ALTER TABLE video_games ADD FOREIGN KEY (na_sales_id) REFERENCES na_sales(NA_sales_id); 
ALTER TABLE video_games ADD FOREIGN KEY (eu_sales_id) REFERENCES eu_sales(EU_sales_id); 
ALTER TABLE video_games ADD FOREIGN KEY (other_sales_id) REFERENCES other_sales(other_sales_id); 
ALTER TABLE video_games ADD FOREIGN KEY (jp_sales_id) REFERENCES jp_sales(JP_sales_id);  
