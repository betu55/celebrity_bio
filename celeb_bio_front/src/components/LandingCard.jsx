import React from "react";
import { Link } from "react-router-dom";

export default function LandingCard(props) {
  const { title } = props;

  return (
    <div className="col-span-1 ">
      <Link
        to={`/${title}`}
        className="bg-red-200 md:w-4/5 py-20 text-cyan-400 text-center md:text-2xl rounded-md block"
      >
        {title}
      </Link>
    </div>
  );
}
