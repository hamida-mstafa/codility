const request = require("supertest");
const app = require(process.env.SERVER_PATH);
const NEW_USER_NAME = "bob zoe";

const assert = require("assert");

describe("API Test", function () {
  this.timeout("60000");
  it("API Test returns JSON with a list of users", async () => {
    const response = await request(app).get("/users");
    assert.equal(response.body.length, 2);
    let count = 0;
    while (count < response.body.length){
      let user = response.body[count];
      assert.notEqual(user.id, null)
      if (user.id == 1){
        assert.equal(user.name, "john doe");
      }
      if (user.id == 2){
        assert.equal(user.name, "anna boe");
      }
      count++;
    }
    assert.equal(response.status, 200);
    assert.equal(response.headers["content-type"].split(";")[0].toLowerCase(), "application/json")
  });

  it("API Test endpoint /new returns expected text", async () => {
    const response = await request(app).get("/new");
    let keys = [];
    for (akey in response.body) {
      keys.push(akey);
    }
    assert.notEqual(keys.indexOf("text"), -1)
    assert.equal(response.body["text"], "welcome to the new page");
  });

  it("API Test endpoint /nonexisting returns 404 status", async function () {
    const response = await request(app).get("/nonexisting");
    assert.equal(response.status, 404);
  });

  it("API Test root path returns redirects", async ()=>{
    const response = await request(app).get("/");
    assert.equal(response.status, 301);
  });

  it("API Test adding new user to the list", async ()=>{
    const response = await request(app).post(`/users`).send({name: NEW_USER_NAME});
    assert.equal(response.status, 200);
    assert.equal(response.text, `${NEW_USER_NAME} has been added to the users list`);
  })
});
