"use client";

import React, { useState } from "react";

export default function Home() {
  const [input, setInput] = useState("");
  const [report, setReport] = useState(null);

  const sendURL = async () => {
    const response = await fetch("http://127.0.0.1:8000/scan", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ url: input }),
    });

    const data = await response.json();

    setReport(data.message);
  };

  return (
    <div>
      <h1 className="heading">Security Report Generator</h1>

      <input value={input} onChange={(e) => setInput(e.target.value)} />

      <button onClick={sendURL}>generate report</button>

      <pre className="report">
        {report ? JSON.stringify(report, null, 2) : ""}
      </pre>
    </div>
  );
}
