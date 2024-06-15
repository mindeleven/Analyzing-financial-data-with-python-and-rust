use std::fs::File;
use chrono::prelude::*;
use polars::prelude::*;

fn main() {
    let mut df: DataFrame = df!(
        "integer" => &[1, 2, 3],
        "date" => &[
            NaiveDate::from_ymd_opt(2025, 1, 1).unwrap().and_hms_opt(0, 0, 0).unwrap(),
            NaiveDate::from_ymd_opt(2025, 1, 2).unwrap().and_hms_opt(0, 0, 0).unwrap(),
            NaiveDate::from_ymd_opt(2025, 1, 3).unwrap().and_hms_opt(0, 0, 0).unwrap(),
        ],
        "float" => &[4.0, 5.0, 6.0],
        "string" => &["a", "b", "c"]
    )
    .unwrap();

    println!("{:?}", df);

    let data_dir = "./data/";

    let output_file = data_dir.to_string() + "output_file_1.csv";

    let mut file = File::create(output_file).expect("could not create file");

    CsvWriter::new(&mut file)
        .include_header(true)
        .with_separator(b',')
        .finish(&mut df)
        .unwrap();
    
    /* let df_csv = CsvReadOptions::default()
        .with_infer_schema_length(None)
        .with_has_header(true)
        .try_into_reader_with_file_path(Some("../../../../assets/data/output.csv".into()))?
        .finish()?;
    */
    
    let input_file = data_dir.to_string() + "output_file_1.csv";

    let df_csv_1 = CsvReader::from_path(input_file)
        .unwrap()
        .has_header(true)
        .finish();

    println!("{:?}", df_csv_1);

}
