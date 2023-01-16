import React from "react";

// Use functional or class component based on your preference.
// Make it a default export.

export default function LoginForm({ onSubmit }) {
  const [name, setName] = React.useState('');
  const [password, setPassword] = React.useState('');

  const buttonDisabled = (name == '' || password == '');

  const submitForm = () => {
    onSubmit(name, password)
  }

  return (
    <form onSubmit={submitForm}>
      <label>
        Username
        <input id="username-input" type="text" value={name} onChange={(e) => setName(e.target.value)} />
      </label><br/>
      <label>
        Password
        <input id="password-input" type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
      </label><br/>
      <button id="login-button" type="submit" disabled={buttonDisabled} onClick={submitForm}>
        Submit
      </button>
    </form>
  );
}