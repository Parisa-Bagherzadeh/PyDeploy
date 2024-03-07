var client = new HttpClient();
var request = new HttpRequestMessage(HttpMethod.Get, "https://api.dictionaryapi.dev/api/v2/entries/en/detach");
var response = await client.SendAsync(request);
response.EnsureSuccessStatusCode();
Console.WriteLine(await response.Content.ReadAsStringAsync());
