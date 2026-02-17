import { motion } from 'framer-motion';
import { HelpCircle, ChevronRight, MessageSquare, AlertTriangle, LifeBuoy, Ghost, Search, BookOpen, Bug, PenTool, LayoutTemplate } from 'lucide-react';

import TelegramWidget from '../components/TelegramWidget';

const REPO_URL = "https://github.com/FaserF/TCL-Discussion-Telegram";

const troubleshooting = [
    {
        code: "Verification Failed",
        cause: "Corrupted ZIP download or incompatible USB filesystem.",
        fix: "Re-download the file (preferably using a PC). Re-format USB to FAT32 using MBR (not GPT)."
    },
    {
        code: "No File Found",
        cause: "File is hidden inside a folder or renamed incorrectly.",
        fix: "Ensure the (.zip or .pkg) is in the root directory. Remove any suffixes like (1) from filename."
    },
    {
        code: "TV Stuck on Logo",
        cause: "Soft-brick due to interrupted update or wrong chipset file.",
        fix: "Use the IMG/PKG method. This forces a low-level format and recovers the OS."
    }
];

const faqs = [
    {
        q: "Why is English the only allowed language?",
        a: "Our community spans 100+ countries. English is the common bridge that allows our international experts to help you. Using other languages fragments the knowledge base."
    },
    {
        q: "Is @FirmwareTCLbot safe to use?",
        a: "Absolutely. It's a community tool that pulls data directly from our verified archives. It identifies your TV by Serial Number to prevent downloading the wrong chipset."
    },
    {
        q: "Can I upgrade from Android 9 to Google TV (Android 11)?",
        a: "Depending on your chipset (like RT51), yes! However, this usually requires an IMG flash rather than a simple OTA update."
    },
    {
        q: "How do I find my Serial Number?",
        a: "Check the sticker on the back of your TV or go to Settings → About → Status. It usually starts with a letter like 'Z' or 'B'."
    },
    {
        q: "What is the Service Menu code?",
        a: "The most common code is '6425' (type it while in the Settings menu). CAUTION: Changing parameters here can permanently damage your panel or motherboard. Only use it to check Panel ID or reset Shop Mode."
    }
];

const FAQ = ({ theme }) => {
    return (
        <div className="relative min-h-screen">
            <div className="bg-mesh opacity-30" />

            <div className="pt-24 sm:pt-32 pb-20 relative z-10 max-w-5xl mx-auto px-4">
                <div className="text-center mb-16 sm:mb-20">
                    <motion.div
                        initial={{ opacity: 0, y: -10 }}
                        animate={{ opacity: 1, y: 0 }}
                        className="flex justify-center mb-6"
                    >
                        <div className="p-3 sm:p-4 rounded-3xl bg-tcl-red/10 border border-tcl-red/20">
                            <LifeBuoy className="text-tcl-red w-8 h-8 sm:w-10 sm:h-10 animate-pulse" />
                        </div>
                    </motion.div>
                    <h1 className="text-4xl sm:text-5xl md:text-7xl font-black mb-6">Knowledge <span className="text-gradient">Base</span></h1>
                    <p className="text-gray-400 text-base sm:text-xl max-w-2xl mx-auto leading-relaxed px-4">
                        Everything from basic group rules to advanced motherboard recovery troubleshooting.
                    </p>
                </div>

                {/* Technical Troubleshooting Section */}
                <section className="mb-24 sm:mb-32">
                    <h2 className="text-xl sm:text-2xl font-bold mb-8 sm:mb-10 flex items-center gap-3">
                        <AlertTriangle className="text-orange-500" />
                        Error Code Troubleshooting
                    </h2>
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                        {troubleshooting.map((item, i) => (
                            <motion.div
                                key={i}
                                initial={{ opacity: 0, scale: 0.95 }}
                                whileInView={{ opacity: 1, scale: 1 }}
                                viewport={{ once: true }}
                                transition={{ delay: i * 0.1 }}
                                className="p-6 sm:p-8 rounded-3xl glass border-orange-500/10 hover:border-orange-500/30 transition-all"
                            >
                                <div className="text-[10px] font-black text-orange-500 uppercase tracking-[0.2em] mb-4">Error: {item.code}</div>
                                <div className="mb-6">
                                    <div className="text-[10px] text-gray-500 mb-1 uppercase font-bold tracking-widest">Common Cause</div>
                                    <div className="text-sm text-gray-300 font-medium">{item.cause}</div>
                                </div>
                                <div className="p-4 rounded-2xl bg-orange-500/5 border border-orange-500/10">
                                    <div className="text-[10px] text-orange-400 mb-1 uppercase font-bold tracking-widest">The Fix</div>
                                    <div className="text-xs sm:text-sm text-gray-400 italic">"{item.fix}"</div>
                                </div>
                            </motion.div>
                        ))}
                    </div>
                </section>

                {/* Contribution Section */}
                <section className="mb-24 sm:mb-32">
                    <div className="p-1 rounded-[2.5rem] bg-gradient-to-r from-tcl-red/30 via-tcl-accent/30 to-purple-500/30">
                        <div className="glass p-8 sm:p-14 rounded-[2.3rem] text-center relative overflow-hidden">
                            <div className="relative z-10">
                                <h2 className="text-2xl sm:text-4xl font-black mb-6 px-4">Found a mistake or have a tip?</h2>
                                <p className="text-gray-400 max-w-2xl mx-auto mb-10 sm:mb-12 text-base sm:text-lg px-4">
                                    This site is built by the community. If you found a typo, a wrong link, or want to share a solution,
                                    you can easily report it to our team.
                                </p>

                                <div className="grid grid-cols-1 sm:grid-cols-3 gap-4 sm:gap-6">
                                    <ContributionButton
                                        icon={<PenTool size={20} />}
                                        label="Fix Text"
                                        desc="Typos/Information"
                                        link={`${REPO_URL}/issues/new?template=content_correction.yml`}
                                        color="border-tcl-red/20 text-tcl-red hover:bg-tcl-red/10"
                                    />
                                    <ContributionButton
                                        icon={<LayoutTemplate size={20} />}
                                        label="Design Feedback"
                                        desc="Layout Issues"
                                        link={`${REPO_URL}/issues/new?template=ui_ux_feedback.yml`}
                                        color="border-purple-500/20 text-purple-400 hover:bg-purple-500/10"
                                    />
                                    <ContributionButton
                                        icon={<Bug size={20} />}
                                        label="Technical Bug"
                                        desc="Something broke"
                                        link={`${REPO_URL}/issues/new?template=technical_bug.yml`}
                                        color="border-orange-500/20 text-orange-400 hover:bg-orange-500/10"
                                    />
                                </div>
                            </div>
                        </div>
                    </div>
                </section>

                {/* Multi-Column FAQ */}
                <section className="mb-24 sm:mb-32 px-2">
                    <h2 className="text-xl sm:text-2xl font-bold mb-8 sm:mb-10 flex items-center gap-3 text-gray-900 dark:text-white">
                        <BookOpen className="text-tcl-red" />
                        Community & Rules
                    </h2>
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6 sm:gap-8">
                        {faqs.map((faq, i) => (
                            <motion.div
                                key={i}
                                initial={{ opacity: 0, y: 10 }}
                                whileInView={{ opacity: 1, y: 0 }}
                                viewport={{ once: true }}
                                className="p-6 sm:p-8 rounded-3xl glass border-white/5"
                            >
                                <h4 className="text-lg sm:text-xl font-bold mb-4 text-gray-900 dark:text-white">{faq.q}</h4>
                                <p className="text-sm sm:text-base text-gray-400 leading-relaxed">{faq.a}</p>
                            </motion.div>
                        ))}
                    </div>
                </section>

                {/* Telegram Redirect */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-12 items-center px-4 sm:px-6">
                    <div className="text-center md:text-left">
                        <h3 className="text-3xl sm:text-4xl font-black mb-6">Didn't find what you need?</h3>
                        <p className="text-gray-400 mb-8 sm:mb-10 text-base sm:text-lg leading-relaxed max-w-lg mx-auto md:mx-0">
                            Our 24/7 moderation team and thousands of active users are ready to help in the discussion group.
                        </p>
                        <div className="flex flex-col sm:flex-row gap-4 justify-center md:justify-start">
                            <a
                                href="https://t.me/tclupdates_discussion"
                                target="_blank"
                                className="px-8 py-4 rounded-2xl bg-tcl-red text-white font-black text-lg hover:scale-105 transition-all shadow-xl flex items-center justify-center gap-2"
                            >
                                Join Support <MessageSquare size={20} />
                            </a>
                            <a
                                href="https://t.me/FirmwareTCLbot"
                                target="_blank"
                                className="px-8 py-4 rounded-2xl glass border border-white/10 text-gray-900 dark:text-white font-bold text-lg hover:bg-white/10 transition-all flex items-center justify-center gap-2"
                            >
                                Ask the Bot <ChevronRight size={20} />
                            </a>
                        </div>
                    </div>
                    <div className="mt-8 md:mt-0 w-full max-w-sm mx-auto">
                        <div className="p-2 rounded-[2rem] bg-gradient-to-br from-tcl-red/20 to-tcl-red/5">
                            <TelegramWidget post="tclupdates/1" width="100%" dark={theme === 'dark'} />
                        </div>
                        <p className="text-[10px] text-gray-500 mt-4 uppercase font-black tracking-widest text-center">Live Preview: Current Firmware Announcements</p>
                    </div>
                </div>
            </div>
        </div>
    );
};

const ContributionButton = ({ icon, label, desc, link, color }) => (
    <a
        href={link}
        target="_blank"
        rel="noopener noreferrer"
        className={`p-6 rounded-2xl border transition-all flex flex-col items-center gap-3 ${color}`}
    >
        {icon}
        <div className="font-bold">{label}</div>
        <div className="text-[10px] uppercase font-bold tracking-widest opacity-60">{desc}</div>
    </a>
);

export default FAQ;
