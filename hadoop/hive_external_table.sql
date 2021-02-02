CREATE EXTERNAL TABLE `covid`(
  `code_dep` bigint, 
  `departement` string, 
  `jour` string, 
  `hosp` bigint, 
  `rad` bigint, 
  `rea` bigint)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\,'
STORED AS TEXTFILE
LOCATION '/user/hive/covid/';



select * from covid;
