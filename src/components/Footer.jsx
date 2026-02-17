import React from 'react';
import { Shield, Globe, Headphones, Heart, Terminal, ExternalLink, Monitor } from 'lucide-react';

const Footer = () => {
    return (
        <footer className="relative mt-20 border-t border-black/5 dark:border-white/5 bg-gray-50 dark:bg-tcl-dark pt-16 sm:pt-20 pb-10 transition-colors">
            <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div className="grid grid-cols-1 md:grid-cols-12 gap-12 mb-16">
                    <div className="md:col-span-5">
                        <div className="flex items-center gap-3 mb-6">
                            <div className="w-8 h-8 rounded-lg bg-gradient-to-br from-tcl-red to-tcl-accent flex items-center justify-center shadow-lg">
                                <Monitor className="text-white w-5 h-5" />
                            </div>
                            <span className="text-gray-900 dark:text-white font-black text-xl">Community <span className="text-tcl-red italic">Resource</span></span>
                        </div>
                        <div className="glass p-6 sm:p-8 rounded-2xl border-white/5 space-y-4">
                            <div className="flex gap-3 text-red-500">
                                <Shield className="shrink-0 w-5 h-5" />
                                <h4 className="font-bold text-[10px] sm:text-xs uppercase tracking-[0.2em]">Legal Notice</h4>
                            </div>
                            <p className="text-xs text-gray-600 dark:text-gray-400 leading-relaxed">
                                This is a community-driven documentation hub. This website and the associated Telegram groups are <strong>NOT official TCL services</strong>.
                                We are enthusiasts helping enthusiasts. All firmware files, documentation, and technical rights mentioned here belong to their respective owners.
                            </p>
                            <div className="pt-4 border-t border-white/5">
                                <p className="text-[10px] text-tcl-red font-black uppercase tracking-widest mb-2">Volunteer Powered</p>
                                <p className="text-[11px] text-gray-500 dark:text-gray-400 leading-relaxed italic">
                                    A massive <strong>thank you</strong> to all administrators and moderators who maintain this community in their free time.
                                </p>
                            </div>
                        </div>
                    </div>

                    <div className="md:col-span-4">
                        <h4 className="text-gray-900 dark:text-white font-black text-xs uppercase tracking-widest mb-6 flex items-center gap-2">
                            <Headphones className="text-tcl-red w-4 h-4" />
                            Official TCL Support
                        </h4>
                        <div className="space-y-3">
                            <a
                                href="https://www.tcl.com/support"
                                target="_blank"
                                rel="noopener noreferrer"
                                className="flex items-center justify-between p-4 rounded-xl border border-black/5 dark:border-white/5 bg-white dark:bg-white/5 hover:border-tcl-red/30 transition-all group"
                            >
                                <span className="text-sm font-medium text-gray-600 dark:text-gray-300">TCL Global Support</span>
                                <Globe className="w-4 h-4 text-gray-400 group-hover:text-tcl-red transition-colors" />
                            </a>
                            <a
                                href="https://support.tcl.com/us"
                                target="_blank"
                                rel="noopener noreferrer"
                                className="flex items-center justify-between p-4 rounded-xl border border-black/5 dark:border-white/5 bg-white dark:bg-white/5 hover:border-tcl-red/30 transition-all group"
                            >
                                <span className="text-sm font-medium text-gray-600 dark:text-gray-300">TCL USA Help Center</span>
                                <Globe className="w-4 h-4 text-gray-400 group-hover:text-tcl-red transition-colors" />
                            </a>
                        </div>
                    </div>

                    <div className="md:col-span-3">
                        <h4 className="text-gray-900 dark:text-white font-black text-xs uppercase tracking-widest mb-6 px-1">Navigation</h4>
                        <ul className="space-y-3 text-sm font-bold text-gray-500">
                            <li><a href="/" className="hover:text-tcl-red transition-colors">Home Hub</a></li>
                            <li><a href="/guides" className="hover:text-tcl-red transition-colors">Encyclopedia</a></li>
                            <li><a href="/faq" className="hover:text-tcl-red transition-colors">Safety FAQ</a></li>
                            <li><a href="https://github.com/FaserF/TCL-Discussion-Telegram/issues/new/choose" target="_blank" className="text-red-400 hover:text-red-300 transition-colors flex items-center gap-1 font-black">Report a Problem <ExternalLink size={12} /></a></li>
                        </ul>
                    </div>
                </div>

                <div className="border-t border-white/5 pt-10 flex flex-col md:flex-row justify-between items-center gap-6">
                    <div className="flex flex-col sm:flex-row items-center gap-2 sm:gap-4 text-[10px] text-gray-500 font-bold uppercase tracking-widest text-center">
                        <span>© {new Date().getFullYear()} Community Team</span>
                        <div className="hidden sm:block w-1 h-1 rounded-full bg-gray-300 dark:bg-gray-800" />
                        <span className="flex items-center gap-1">Built with <Heart className="w-3 h-3 text-red-500 fill-red-500/30" /> by volunteers</span>
                    </div>
                    <div className="flex gap-6">
                        <a href="https://t.me/tclupdates" className="text-[10px] font-black uppercase tracking-widest text-gray-500 hover:text-tcl-red transition-colors">Channel</a>
                        <a href="https://t.me/tclupdates_discussion" className="text-[10px] font-black uppercase tracking-widest text-gray-500 hover:text-tcl-red transition-colors">Group</a>
                        <a href="https://t.me/FirmwareTCLbot" className="text-[10px] font-black uppercase tracking-widest text-gray-500 hover:text-tcl-red transition-colors">Bot</a>
                    </div>
                </div>
            </div>
        </footer>
    );
};

export default Footer;
