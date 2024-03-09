var client = new HttpClient();
var request = new HttpRequestMessage(HttpMethod.Get, "https://alquran.cloud/api");
var response = await client.SendAsync(request);
response.EnsureSuccessStatusCode();
Console.WriteLine(await response.Content.ReadAsStringAsync());
