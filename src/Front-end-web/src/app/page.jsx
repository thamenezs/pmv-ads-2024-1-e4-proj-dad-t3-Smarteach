'use client'
import ClassList from "@/components/class-list";
import Mural from "@/components/mural";

export default function Home() { 

  return (
    <div className="w-full h-full flex flex-col justify-center items-center gap-10">
      <h1 className="text-2xl"> Turmas </h1>
      <div className="flex">
        <ClassList />
        <Mural />
      </div>
    </div>
  );
}