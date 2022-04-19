import React, { useState } from "react";
import "../sass/main.scss";

function PostForm() {
  const [data, setdata] = useState({
    fullName: "",
    zipcode: "",
    zipcodeValid: false,
  });
  const [output, setoutput] = useState({
    result: "",
  });
  // function to fetch output
  async function fetchOutput() {
    const response = await fetch("/create_phrase", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        fullName: data.fullName,
        zipcode: data.zipcode,
      }),
    });
    const result = await response.text();
    return result;
  }
  // function to validate zipcode
  function validate_zipcode(zipcode) {
    if (zipcode.length === 5 && parseFloat(zipcode)) {
      return true;
    }
    return false;
  }
  //handling submit button function
  const handleSubmit = (e) => {
    e.preventDefault();
    if (validate_zipcode(data.zipcode)) {
      fetchOutput().then((out) => setoutput({ result: out }));
    } else {
      alert("Enter valid zipcode");
    }
  };

  return (
    <div className="form-class">
      <div className="form-title">Zero Coding Challenge</div>
      <form className="form-body" onSubmit={handleSubmit}>
        <label htmlFor="fullName">Full Name</label>
        <br />
        <input
          type="text"
          name="fullName"
          value={data.fullName}
          onChange={(e) => setdata({ ...data, fullName: e.target.value })}
          required
        />
        <br />
        <br />
        <label htmlFor="zipcode">Zip Code</label>
        <br />
        <input
          type="text"
          name="zipcode"
          value={data.zipcode}
          onChange={(e) => setdata({ ...data, zipcode: e.target.value })}
          required
        />
        <br />
        <br />
        <div className="rule"></div>
        <button className="button-body" type="submit">
          Submit
        </button>
      </form>
      <br />
      <br />
      <div className="output-form">
        <h3>Output</h3>
        {output.result}
      </div>
    </div>
  );
}
export default PostForm;
