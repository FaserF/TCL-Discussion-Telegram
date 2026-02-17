import React from 'react';
import { motion } from 'framer-motion';
import { Terminal, Github, GitPullRequest, Eye, Zap, MessageSquare, ArrowRight, Heart, Code, Layers } from 'lucide-react';

const Contribute = () => {
    const steps = [
        {
            icon: <Terminal className="text-tcl-red" size={24} />,
            title: "Clone the Repository",
            desc: "Use Git to download the code to your local machine. If you don't have Git, download the ZIP from GitHub.",
            code: "git clone https://github.com/FaserF/TCL-Discussion-Telegram"
        },
        {
            icon: <Zap className="text-tcl-red" size={24} />,
            title: "Run the Dev Script",
            desc: "We made it simple. Just right-click 'dev.ps1' and 'Run with PowerShell'. It installs everything and opens the site.",
            code: "./dev.ps1"
        },
        {
            icon: <Code className="text-tcl-red" size={24} />,
            title: "Make Your Changes",
            desc: "Open the project in VS Code. All documentation is in 'src/pages'. Edit the text and see live updates in your browser.",
        },
        {
            icon: <GitPullRequest className="text-tcl-red" size={24} />,
            title: "Submit a PR",
            desc: "Push your changes to your fork and create a Pull Request. Our automated checks will verify everything is perfect.",
        }
    ];

    return (
        <div className="relative min-h-screen">
            <div className="bg-mesh opacity-30" />

            <div className="pt-32 pb-20 relative z-10 max-w-5xl mx-auto px-4">
                <header className="text-center mb-20">
                    <motion.div
                        initial={{ opacity: 0, scale: 0.8 }}
                        animate={{ opacity: 1, scale: 1 }}
                        className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-tcl-red/10 border border-tcl-red/20 text-tcl-red text-[10px] font-black uppercase tracking-[0.2em] mb-6"
                    >
                        <Heart className="w-3 h-3 fill-tcl-red" />
                        Join the Mission
                    </motion.div>
                    <h1 className="text-5xl md:text-7xl font-black mb-6 tracking-tight">
                        How to <span className="text-gradient">Contribute</span>
                    </h1>
                    <p className="text-xl text-gray-400 max-w-2xl mx-auto leading-relaxed">
                        You don't need to be a software engineer to help. Whether it's fixing a typo,
                        adding a new chipset, or updating an FAQ, every contribution matters.
                    </p>
                </header>

                <div className="grid grid-cols-1 gap-8 mb-32">
                    {steps.map((step, i) => (
                        <motion.div
                            key={i}
                            initial={{ opacity: 0, y: 20 }}
                            whileInView={{ opacity: 1, y: 0 }}
                            viewport={{ once: true }}
                            transition={{ delay: i * 0.1 }}
                            className="glass p-10 rounded-[2.5rem] border-white/5 flex flex-col md:flex-row gap-8 items-start hover:border-tcl-red/20 transition-all group"
                        >
                            <div className="w-16 h-16 rounded-2xl bg-white/5 flex items-center justify-center shrink-0 group-hover:bg-tcl-red/10 transition-all">
                                {step.icon}
                            </div>
                            <div className="flex-1">
                                <h3 className="text-2xl font-bold text-gray-900 dark:text-white mb-3 flex items-center gap-3">
                                    <span className="text-tcl-red opacity-20 text-4xl font-black">0{i + 1}</span> {step.title}
                                </h3>
                                <p className="text-gray-400 leading-relaxed mb-6">{step.desc}</p>
                                {step.code && (
                                    <div className="bg-black/5 dark:bg-black/60 rounded-xl p-4 border border-black/5 dark:border-white/5 font-mono text-sm text-tcl-red flex justify-between items-center">
                                        <code>{step.code}</code>
                                        <Layers size={14} className="opacity-40" />
                                    </div>
                                )}
                            </div>
                        </motion.div>
                    ))}
                </div>

                {/* Advanced Info */}
                <section className="mb-32 grid grid-cols-1 md:grid-cols-2 gap-8">
                    <div className="glass p-10 rounded-[2.5rem] border-white/5">
                        <div className="flex items-center gap-3 text-tcl-red font-black text-xs uppercase tracking-widest mb-6">
                            <Github size={16} /> Repository Structure
                        </div>
                        <ul className="space-y-4 text-sm font-medium">
                            <li className="flex items-center gap-3 text-gray-300">
                                <span className="w-1.5 h-1.5 rounded-full bg-tcl-red" />
                                src/pages/FAQ.jsx — All troubleshooting content
                            </li>
                            <li className="flex items-center gap-3 text-gray-300">
                                <span className="w-1.5 h-1.5 rounded-full bg-tcl-red" />
                                src/pages/FlashingGuide.jsx — Chipset technical info
                            </li>
                            <li className="flex items-center gap-3 text-gray-300">
                                <span className="w-1.5 h-1.5 rounded-full bg-tcl-red" />
                                src/data/searchData.js — Global search index
                            </li>
                        </ul>
                    </div>

                    <div className="glass p-10 rounded-[2.5rem] border-white/5">
                        <div className="flex items-center gap-3 text-purple-400 font-black text-xs uppercase tracking-widest mb-6">
                            <Zap size={16} /> Code Standards
                        </div>
                        <p className="text-sm text-gray-400 leading-relaxed mb-6">
                            We use Tailwind CSS for styling and Framer Motion for animations.
                            If you add a new chipset, please also update the search index in <code>searchData.js</code>.
                        </p>
                        <div className="p-4 rounded-xl bg-purple-500/5 border border-purple-500/10 text-xs text-purple-300 italic text-center">
                            "Perfect is the enemy of good. Just submit your edit and we'll polish it together!"
                        </div>
                    </div>
                </section>

                <div className="text-center">
                    <a
                        href="https://github.com/FaserF/TCL-Discussion-Telegram"
                        target="_blank"
                        className="px-10 py-5 rounded-2xl bg-gray-900 dark:bg-white text-white dark:text-black font-black text-lg hover:scale-105 transition-all shadow-xl flex items-center justify-center gap-2 mx-auto inline-flex"
                    >
                        <Github /> Open GitHub Repository <ArrowRight />
                    </a>
                </div>
            </div>
        </div>
    );
};

export default Contribute;
