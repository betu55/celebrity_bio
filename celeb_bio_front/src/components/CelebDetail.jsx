import React, { useState } from "react";

export default function CelebDetail(props) {
  return (
    <>
      <div className="row-start-2 col-span-3 col-start-2 card-bg px-2 py-4 font-bold text-gray-600">
        <div className="card-text">
          Name: <div>{props.data.name}</div>
        </div>
        <div className="card-text">
          Birth day: <div>{props.data.birth_date}</div>
        </div>
        <div className="card-text">
          Sex: <div>{props.data.sex}</div>
        </div>
      </div>
      <div className="row-start-2 col-span-7 col-start-5 card-bg px-2 py-4 font-bold text-gray-600"></div>

      <div className="row-start-3 col-span-5 col-start-2 card-bg px-2 py-4 font-bold text-gray-600"></div>
      <div className="row-start-3 col-span-3 col-start-9 card-bg px-2 py-4 font-bold text-gray-600"></div>
      <div className="row-start-3 col-span-2 col-start-7 card-bg px-2 py-4 font-bold text-gray-600"></div>
    </>
  );
}
