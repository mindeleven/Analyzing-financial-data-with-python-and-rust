/// Short example on how to use the Financial Modeling Prep Web API | Rust SDK
/// https://site.financialmodelingprep.com/developer/docs
/// https://crates.io/crates/fmp
/// https://github.com/fcote/fmp-rs
/// https://docs.rs/fmp/latest/fmp/
/// https://docs.rs/fmp/latest/fmp/historical_price/struct.FMPHistoricalPriceResponse.html
use fmp::Client;
use fmp::period::FMPPeriod;
use std::fs;

#[tokio::main]
async fn main() {
    // getting the api key from the abyss of our file system
    let api_key = fs::read_to_string(
            "../../../../../../../tmp/access_data/fmp_api_key.txt"
        )
        .expect("Unable to read file");
    
    // creating an instance of the Client struct from FMP
    let c: Client = Client {
        // setting the base field to the base URL for the FMP API 
        base: "https://financialmodelingprep.com/api/".to_string(),
        api_key: api_key.to_string(),
    };
    
    // requests to the FMP API can be made via the client struct
    // requesting historical data for Netflix, ticker symbol NFLX
    // historical_prices() returns a vector with the stock price data
    let stock_price_data = c.historical_prices("NFLX")
        // 
        .await
        .expect("Couldn't load data for the specified ticker");
    // println!("{:#?}", stock_price_data);
    // first entry of the assets historical price
    println!("{:#?}", stock_price_data.get(0));

}
