import Sidebar from "../components/layout/Sidebar";
import Header from "../components/layout/Header";
import Hero from "../components/hero/Hero";
import PromptBar from "../components/common/PromptBar";

export default function Dashboard() {
  return (
    <div className="h-screen flex bg-slate-100">

      <Sidebar />

      <div className="flex-1 flex flex-col">

        <Header />

        <div className="flex-1 overflow-auto">

          <Hero />

        </div>

        <PromptBar />

      </div>

    </div>
  );
}