import React, { useState } from "react";
import "./data.css";
import { CopyToClipboard } from "react-copy-to-clipboard";

const Data = () => {
  // let history = useHistory();
  const [data, setData] = useState([]);
  const [credentials, setCredentials] = useState({
    passw: "",
  });
  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await fetch(`http://127.0.0.1:8080/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        //    "auth-token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjp7ImlkIjoiNjEzNDRiYzFhZTc4NzRiZTA3M2JiYWJmIn0sImlhdCI6MTYzMTAwODU5OX0.fFdZmMml4_Wzw_TxMhGoiWiqGriA9JX8naTIoQGpO4o"
      },
      body: JSON.stringify({
        pass: credentials.passw,
      }),
    });
    const json = await response.json();
    localStorage.removeItem("password");
    console.log(json.passw);
    setData(json);
    localStorage.setItem("password", json.passw);
    window.location.reload();

    // alert("Booking is done");
  };
  const onChange = (e) => {
    setCredentials({ ...credentials, [e.target.name]: e.target.value });
  };
  console.log();
  const token = localStorage.getItem("password");

  return (
      <>
          <div className="box1">
          <h1 className="center">Encrypt your Password</h1>
      <div className="container-fluid">
        <form onSubmit={handleSubmit}>
          <div className="mb-3">
            <label htmlFor="passw" className="form-label">
              Password
            </label>
            <input
              type="text"
              className="form-control"
              value={credentials.passw}
              onChange={onChange}
              id="passw"
              name="passw"
              // aria-describedby="emailHelp"
            />
          </div>

          <button type="submit" className="btn btn-primary">
            Submit
          </button>
        </form>
        {/* {
                    data && data.length > 0 && data.map((item) => <h1>{item.passw}</h1>)
                } */}
        <div className="box">
          <h1 id="copy">{token}</h1>
        </div>
              <CopyToClipboard text={token}>
          <button>Copy to clipboard</button>
        </CopyToClipboard>
              </div>
                </div>
      {/* <Test/> */}
    </>
  );
  // window.location.reload();
};

export default Data;
