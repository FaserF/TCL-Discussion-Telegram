import React from 'react';
import { motion } from 'framer-motion';
import { Download, Bot, MessageCircle, ArrowRight, ShieldAlert, Cpu, Layers, Zap, MessageSquare, Megaphone, Headphones, ExternalLink, Heart } from 'lucide-react';
import { Link } from 'react-router-dom';
import TelegramWidget from '../components/TelegramWidget';

const Home = ({ theme }) => {
    return (
        <div className="relative min-h-screen">
            <div className="bg-mesh" />

            <div className="pt-24 sm:pt-32 pb-20 relative z-10">
                <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
                    <motion.div
                        initial={{ opacity: 0, scale: 0.8 }}
                        animate={{ opacity: 1, scale: 1 }}
                        transition={{ duration: 0.5 }}
                        className="mb-8 sm:mb-10"
                    >
                        <span className="inline-flex items-center space-x-2 px-4 py-1.5 rounded-full bg-tcl-red/10 border border-tcl-red/20 text-tcl-red text-[10px] sm:text-xs font-bold uppercase tracking-widest">
                            <Zap className="w-3 h-3 fill-tcl-red" />
                            <span>Community Hub</span>
                        </span>
                    </motion.div>

                    <motion.h1
                        initial={{ opacity: 0, y: 30 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ duration: 0.8, ease: "easeOut" }}
                        className="text-4xl sm:text-6xl md:text-8xl font-extrabold tracking-tight mb-6 sm:mb-8 leading-[1.1] px-2"
                    >
                        Unlock the Full Power of <br className="hidden sm:block" />
                        <span className="text-gradient inline-block mt-2 sm:mt-0">Your TCL TV</span>
                    </motion.h1>

                    <motion.p
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: 0.2, duration: 0.8 }}
                        className="max-w-2xl mx-auto text-base sm:text-xl text-gray-400 mb-10 sm:mb-12 leading-relaxed px-4"
                    >
                        Access exclusive firmware updates, expert flashing guides, and
                        join thousands of enthusiasts in the world's largest TCL discussion group.
                    </motion.p>

                    <motion.div
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: 0.4, duration: 0.8 }}
                        className="flex flex-col sm:flex-row items-center justify-center gap-4 sm:gap-6 px-4"
                    >
                        <Link to="/guides" className="group w-full sm:w-auto px-8 sm:px-10 py-4 sm:py-5 rounded-2xl bg-tcl-red text-white font-bold text-base sm:text-lg hover:scale-105 active:scale-95 transition-all shadow-xl glow flex items-center justify-center gap-2">
                            Explore Guides <ArrowRight className="group-hover:translate-x-1 transition-transform" />
                        </Link>
                        <a href="https://t.me/tclupdates" target="_blank" className="w-full sm:w-auto px-8 sm:px-10 py-4 sm:py-5 rounded-2xl glass border border-black/10 dark:border-white/10 text-gray-900 dark:text-white font-bold text-base sm:text-lg hover:bg-black/5 dark:hover:bg-white/10 transition-all flex items-center justify-center gap-2 font-bold">
                            <Download className="w-5 h-5" /> Get Firmwares
                        </a>
                    </motion.div>
                </section>

                <section className="max-w-7xl mx-auto px-4 mt-24 sm:mt-32">
                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6 sm:gap-8">
                        <motion.a
                            href="https://t.me/tclupdates_discussion"
                            target="_blank"
                            initial={{ opacity: 0, x: -20 }}
                            whileInView={{ opacity: 1, x: 0 }}
                            viewport={{ once: true }}
                            className="p-1 rounded-[2rem] bg-gradient-to-br from-tcl-red/20 to-tcl-accent/20 group overflow-hidden relative min-h-[280px]"
                        >
                            <div className="absolute top-0 right-0 p-8 opacity-10 group-hover:scale-110 transition-transform">
                                <MessageSquare size={120} />
                            </div>
                            <div className="glass h-full p-8 sm:p-10 rounded-[1.8rem] flex flex-col justify-between items-start relative z-10">
                                <div>
                                    <div className="flex items-center gap-2 text-tcl-red font-black text-[10px] sm:text-xs uppercase tracking-widest mb-4">
                                        <MessageSquare size={14} /> The Group
                                    </div>
                                    <h3 className="text-3xl sm:text-4xl font-black text-gray-900 dark:text-white mb-4">Join Discussion</h3>
                                    <p className="text-gray-400 font-medium text-sm sm:text-base">Get live help, share your setup, and talk to experts.</p>
                                </div>
                                <div className="mt-8 flex items-center gap-2 text-gray-900 dark:text-white font-bold group-hover:gap-4 transition-all text-sm sm:text-base">
                                    t.me/tclupdates_discussion <ArrowRight size={20} />
                                </div>
                            </div>
                        </motion.a>

                        <motion.a
                            href="https://t.me/tclupdates"
                            target="_blank"
                            initial={{ opacity: 0, x: 20 }}
                            whileInView={{ opacity: 1, x: 0 }}
                            viewport={{ once: true }}
                            className="p-1 rounded-[2rem] bg-gradient-to-br from-purple-500/40 to-pink-500/40 group overflow-hidden relative min-h-[280px]"
                        >
                            <div className="absolute top-0 right-0 p-8 opacity-10 group-hover:scale-110 transition-transform">
                                <Megaphone size={120} />
                            </div>
                            <div className="glass h-full p-8 sm:p-10 rounded-[1.8rem] flex flex-col justify-between items-start relative z-10">
                                <div>
                                    <div className="flex items-center gap-2 text-purple-400 font-black text-[10px] sm:text-xs uppercase tracking-widest mb-4">
                                        <Megaphone size={14} /> The Channel
                                    </div>
                                    <h3 className="text-3xl sm:text-4xl font-black text-gray-900 dark:text-white mb-4">Update Feed</h3>
                                    <p className="text-gray-400 font-medium text-sm sm:text-base">The fastest source for new firmware releases.</p>
                                </div>
                                <div className="mt-8 flex items-center gap-2 text-gray-900 dark:text-white font-bold group-hover:gap-4 transition-all text-sm sm:text-base">
                                    t.me/tclupdates <ArrowRight size={20} />
                                </div>
                            </div>
                        </motion.a>
                    </div>
                </section>

                <section className="max-w-7xl mx-auto px-4 mt-24 sm:mt-32">
                    <div className="grid grid-cols-1 lg:grid-cols-12 gap-8 sm:gap-12 items-start">
                        <div className="lg:col-span-8">
                            <div className="glass p-8 sm:p-12 rounded-[2.5rem] sm:rounded-[3rem] border-white/5 relative overflow-hidden h-full">
                                <div className="flex flex-col md:flex-row items-center justify-between gap-10">
                                    <div className="max-w-xl text-center md:text-left">
                                        <h2 className="text-2xl sm:text-3xl font-black mb-6 flex items-center justify-center md:justify-start gap-3 text-gray-900 dark:text-white">
                                            <Headphones className="text-tcl-red w-8 h-8" />
                                            Need Official Support?
                                        </h2>
                                        <p className="text-gray-400 leading-relaxed mb-8 text-sm sm:text-base">
                                            While our community is great for technical enthusiasts, official warranty or hardware repairs
                                            should always be handled by the manufacturer directly.
                                        </p>
                                        <div className="flex flex-wrap justify-center md:justify-start gap-4">
                                            <a href="https://www.tcl.com/support" target="_blank" rel="noopener noreferrer" className="px-6 py-3 rounded-xl bg-black/5 dark:bg-white/5 border border-black/10 dark:border-white/10 text-gray-900 dark:text-white font-bold hover:bg-black/10 dark:hover:bg-white/10 transition-all flex items-center gap-2 hover:text-tcl-red text-sm">
                                                Support Site <ExternalLink size={16} />
                                            </a>
                                            <a href="https://support.tcl.com/us" target="_blank" className="px-6 py-3 rounded-xl bg-black/5 dark:bg-white/5 border border-black/10 dark:border-white/10 text-gray-900 dark:text-white font-bold hover:bg-black/10 dark:hover:bg-white/10 transition-all flex items-center gap-2 text-sm">
                                                Local Support Centre <ExternalLink size={16} />
                                            </a>
                                        </div>
                                    </div>
                                    <div className="w-full md:w-auto">
                                        <a href="https://www.tcl.com/support" target="_blank" rel="noopener noreferrer" className="p-6 rounded-2xl border border-white/5 bg-black/40 text-center block hover:border-tcl-red/30 transition-all group">
                                            <div className="text-[10px] font-bold text-gray-500 uppercase tracking-widest mb-1">Manufacturer Support</div>
                                            <div className="text-tcl-red font-bold group-hover:underline text-sm">tcl.com/support</div>
                                        </a>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className="lg:col-span-4 space-y-8 w-full">
                            <div className="space-y-4">
                                <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-tcl-red/10 border border-tcl-red/20 text-tcl-red text-[10px] font-black uppercase tracking-[0.2em]">
                                    <Megaphone className="w-3 h-3 fill-tcl-red" />
                                    Announcements
                                </div>
                                <TelegramWidget post="tclupdates/1" width="100%" dark={theme === 'dark'} />
                                <p className="text-[10px] text-gray-500 italic text-center uppercase font-bold tracking-widest">
                                    Direct feed from the firmware archive channel.
                                </p>
                            </div>

                            <div className="space-y-4 pt-4 border-t border-white/5">
                                <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-purple-500/10 border border-purple-500/20 text-purple-400 text-[10px] font-black uppercase tracking-[0.2em]">
                                    <MessageSquare className="w-3 h-3 fill-purple-500" />
                                    Live Discussion
                                </div>
                                <TelegramWidget post="tclupdates_discussion/1" width="100%" dark={theme === 'dark'} discussion={true} />
                                <p className="text-[10px] text-gray-500 italic text-center uppercase font-bold tracking-widest">
                                    Real-time help from 50,000+ members.
                                </p>
                            </div>
                        </div>
                    </div>
                </section>

                <section className="max-w-7xl mx-auto px-4 mt-24 sm:mt-32">
                    <motion.div
                        initial={{ opacity: 0, y: 20 }}
                        whileInView={{ opacity: 1, y: 0 }}
                        viewport={{ once: true }}
                        className="glass p-8 sm:p-12 rounded-[2.5rem] sm:rounded-[3.5rem] border-white/5 text-center relative overflow-hidden group"
                    >
                        <div className="absolute inset-0 bg-gradient-to-br from-tcl-red/5 to-tcl-accent/5 opacity-0 group-hover:opacity-100 transition-opacity" />
                        <div className="relative z-10">
                            <div className="inline-flex items-center gap-2 px-4 py-1.5 rounded-full bg-tcl-red/10 border border-tcl-red/20 text-tcl-red text-[10px] font-black uppercase tracking-[0.2em] mb-8">
                                <Heart className="w-3 h-3 fill-tcl-red" />
                                Community Heroes
                            </div>
                            <h2 className="text-3xl sm:text-5xl font-black text-gray-900 dark:text-white mb-6">Built by Volunteers</h2>
                            <p className="text-base sm:text-xl text-gray-400 max-w-2xl mx-auto leading-relaxed mb-10 px-4">
                                This entire ecosystem—the website, the bots, and the support groups—is maintained by a dedicated team of
                                <strong className="text-gray-900 dark:text-white"> administrators and moderators</strong> who contribute their knowledge and
                                <strong className="text-gray-900 dark:text-white"> free time</strong> for the benefit of all TCL users.
                            </p>
                            <div className="flex flex-col items-center gap-4">
                                <div className="text-[10px] font-bold text-gray-500 uppercase tracking-widest">A Huge Thank You To The Team</div>
                                <div className="flex gap-2">
                                    {[1, 2, 3, 4, 5].map((_, i) => (
                                        <div key={i} className="w-2 h-2 rounded-full bg-tcl-red/30" />
                                    ))}
                                </div>
                            </div>
                        </div>
                    </motion.div>
                </section>
            </div>
        </div>
    );
};

export default Home;
