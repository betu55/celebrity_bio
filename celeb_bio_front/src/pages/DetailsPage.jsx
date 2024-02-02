import React, { useEffect, useState } from "react";
import SearchBar from "../components/SearchBar";
import CelebDetail from "../components/CelebDetail";

export default function DetailsPage() {
  const [data, setData] = useState();

  const searchData = (responseData) => {
    setData(responseData);
  };

  return (
    <div className="bg grid grid-cols-12 grid-rows-5 h-screen">
      <div className="col-span-10 col-start-2 text-center text-gray-100">
        <div className="grid grid-rows-3 h-full">
          <div className="self-center">
            <SearchBar toParent={searchData}></SearchBar>
          </div>
          <span className=" text-gray-500 self-center text-lg md:text-3xl font-extrabold">
            This is the details page
          </span>
        </div>
      </div>

      {/* making sure that there is data before trying to pass data to component */}
      {data ? <CelebDetail data={data.information} /> : null}
    </div>
  );
}
