/// https://blog.logrocket.com/making-http-requests-rust-reqwest/

// tokio let's us use "async" on our main function
#[tokio::main]
async fn main() {
    // chaining .await will yield our query result
    let response = reqwest::get("https://api.coinbase.com/v2/prices/spot?currency=USD")
        .await
        // each response is wrapped in a `Result` type
        // we'll unwrap here for simplicity
        .unwrap()
        .text()
        .await;

    println!("{:?}", response);

}