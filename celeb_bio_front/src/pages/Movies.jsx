import React, { useState, useEffect } from "react";
// import { Link } from "react-router-dom";
import SearchBar from "../components/SearchBar";
import { Link } from "react-router-dom";

export default function Movies() {
  const [data, setData] = useState();

  const updateChildData = (data) => {
    setData(data);
  };

  return (
    <div className="h-screen bg grid grid-cols-10 grid-rows-3 md:grid-cols-8 md:grid-rows-5 2xl:grid-cols-11">
      <div className="col-start-2 row-start-2 col-span-8 md:mt-auto md:col-span-4 md:col-start-3 2xl:col-span-5 2xl:col-start-4">
        <SearchBar toParent={updateChildData} />
      </div>
      <div className="row-start-2 mx-auto">{data}</div>
    </div>
  );
}
