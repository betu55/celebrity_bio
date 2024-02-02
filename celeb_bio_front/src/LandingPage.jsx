import React from "react";
import { useState, useEffect } from "react";
import axios from "axios";
// import { Link } from "react-router-dom";
import LandingCard from "./components/LandingCard";

export default function LandingPage() {
  const [links, setLinks] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:8000/api/celebs/")
      .then((response) => {
        setLinks(response.data);
        console.log(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  }, []);

  return (
    <>
      <div className="h-screen bg grid grid-cols-4 grid-rows-3 gap-2">
        {links.map((link) => {
          return <LandingCard title={link.name} key={link.id}></LandingCard>;
        })}
      </div>
    </>
  );
}
