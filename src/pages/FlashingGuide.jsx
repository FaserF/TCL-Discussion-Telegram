import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import {
    Usb, HardDrive, Info, CheckCircle2,
    Cpu, AlertCircle, ChevronDown, ChevronUp,
    Monitor, Smartphone, Terminal, ShieldCheck
} from 'lucide-react';

const chipsets = [
    { name: 'MT9615 (T615T03)', models: 'C735, C835, C935, X925', type: 'Premium Google TV (144Hz)' },
    { name: 'RT51 (R51MT05)', models: 'C725, C825, P725, P8M', type: 'Mainstream Google TV' },
    { name: 'NT72671 (T615T01)', models: 'P635, P735, C635', type: 'Mid-Range Google TV' },
    { name: 'MT5889 (V8-T658T01)', models: 'P815, C715, C815', type: 'Legacy Android TV (4K)' },
    { name: 'RT28xx (R28MT01)', models: 'S615, S5200', type: 'FHD Android TV' },
    { name: 'MT9602 (T615T02)', models: 'P725 (Region Specific)', type: 'Budget Google TV' },
    { name: 'MT5891', models: 'Older 4K Models', type: 'Legacy Android 8/9' },
];

const FlashingGuide = () => {
    const [activeChipset, setActiveChipset] = useState(null);

    return (
        <div className="relative min-h-screen">
            <div className="bg-mesh opacity-50" />

            <div className="pt-24 sm:pt-32 pb-20 relative z-10 max-w-6xl mx-auto px-4">
                <header className="mb-12 sm:mb-20 text-center md:text-left font-black tracking-tight px-2">
                    <h1 className="text-4xl sm:text-5xl md:text-7xl font-black mb-6">
                        Technical <span className="text-gradient">Encyclopedia</span>
                    </h1>
                </header>

                {/* Comparison Matrix */}
                <section className="mb-24 sm:mb-32">
                    <h2 className="text-xl sm:text-2xl font-bold mb-8 sm:mb-10 flex items-center gap-3 px-2">
                        <Monitor className="text-tcl-red" />
                        Comparison: OTA vs IMG
                    </h2>
                    <div className="overflow-x-auto rounded-3xl border border-white/5 glass -mx-2 sm:mx-0">
                        <table className="w-full text-left border-collapse min-w-[600px]">
                            <thead>
                                <tr className="border-b border-white/5 bg-white/5">
                                    <th className="p-4 sm:p-6 text-[10px] sm:text-sm font-bold uppercase tracking-wider text-gray-500">Feature</th>
                                    <th className="p-4 sm:p-6 text-[10px] sm:text-sm font-bold uppercase tracking-wider text-tcl-red">OTA (Local Update)</th>
                                    <th className="p-4 sm:p-6 text-[10px] sm:text-sm font-bold uppercase tracking-wider text-orange-400">IMG / PKG (Flash)</th>
                                </tr>
                            </thead>
                            <tbody className="text-gray-300 text-sm sm:text-base">
                                <tr className="border-b border-white/5">
                                    <td className="p-4 sm:p-6 font-bold">Data Safety</td>
                                    <td className="p-4 sm:p-6"><span className="text-green-400 border border-green-400/20 px-3 py-1 rounded-full text-[10px] sm:text-xs">Safe - Keeps Data</span></td>
                                    <td className="p-4 sm:p-6"><span className="text-red-400 border border-red-400/20 px-3 py-1 rounded-full text-[10px] sm:text-xs font-bold uppercase">Wipe - Factory Reset</span></td>
                                </tr>
                                <tr className="border-b border-white/5">
                                    <td className="p-4 sm:p-6 font-bold">File Formats</td>
                                    <td className="p-4 sm:p-6">One single .zip file</td>
                                    <td className="p-4 sm:p-6">Unzipped .img, .pkg, or .bin</td>
                                </tr>
                                <tr className="border-b border-white/5">
                                    <td className="p-4 sm:p-6 font-bold">Trigger Method</td>
                                    <td className="p-4 sm:p-6">TV Menu → Update → Local</td>
                                    <td className="p-4 sm:p-6">Power Button / Manual Trigger</td>
                                </tr>
                                <tr>
                                    <td className="p-4 sm:p-6 font-bold">Use Case</td>
                                    <td className="p-4 sm:p-6">Normal Upgrade</td>
                                    <td className="p-4 sm:p-6">Downgrade / Recovery</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </section>

                {/* Chipset Explorer */}
                <section className="mb-24 sm:mb-32">
                    <div className="flex flex-col sm:flex-row justify-between items-start sm:items-end mb-8 sm:mb-10 px-2 gap-4">
                        <div>
                            <h2 className="text-xl sm:text-2xl font-bold mb-2 flex items-center gap-3">
                                <Cpu className="text-purple-400" />
                                technical Chipset directory
                            </h2>
                            <p className="text-sm text-gray-500 max-w-lg mb-2">
                                Identified by firmware strings like V8-T615T03. This list is community-sourced and <strong>may not be 100% exhaustive</strong>.
                            </p>
                            <div className="flex items-center gap-2 text-[10px] bg-purple-500/10 text-purple-300 px-3 py-1 rounded-full w-fit font-bold uppercase tracking-wider">
                                <Info size={12} /> Always verify your SN with the bot
                            </div>
                        </div>
                        <a href="https://t.me/FirmwareTCLbot" className="flex items-center gap-2 text-purple-400 font-bold hover:underline text-sm">
                            Check via Bot <ArrowRight size={14} />
                        </a>
                    </div>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4 sm:gap-6">
                        {chipsets.map((c, i) => (
                            <motion.div
                                key={i}
                                whileHover={{ scale: 1.02 }}
                                onClick={() => setActiveChipset(activeChipset === i ? null : i)}
                                className="glass p-5 sm:p-6 rounded-2xl border-white/5 cursor-pointer transition-all"
                            >
                                <div className="flex justify-between items-center">
                                    <div>
                                        <h4 className="text-base sm:text-lg font-extrabold text-gray-900 dark:text-white">{c.name}</h4>
                                        <p className="text-[10px] sm:text-sm text-tcl-red font-medium uppercase tracking-widest">{c.type}</p>
                                    </div>
                                    {activeChipset === i ? <ChevronUp className="text-gray-500" /> : <ChevronDown className="text-gray-500" />}
                                </div>
                                <AnimatePresence>
                                    {activeChipset === i && (
                                        <motion.div
                                            initial={{ height: 0, opacity: 0 }}
                                            animate={{ height: 'auto', opacity: 1 }}
                                            exit={{ height: 0, opacity: 0 }}
                                            className="overflow-hidden"
                                        >
                                            <div className="pt-4 mt-4 border-t border-white/5">
                                                <div className="text-[10px] text-gray-500 mb-2 uppercase font-bold tracking-widest">Typical Models</div>
                                                <div className="text-sm sm:text-base text-gray-300 font-bold">{c.models}</div>
                                                <div className="mt-4 p-3 rounded-xl bg-purple-500/10 border border-purple-500/20 text-[10px] sm:text-xs text-purple-300 font-medium">
                                                    Recommended: Always check your 'Software Version' in About menu. V8-T615T03... corresponds to MT9615.
                                                </div>
                                            </div>
                                        </motion.div>
                                    )}
                                </AnimatePresence>
                            </motion.div>
                        ))}
                    </div>
                </section>

                {/* Detailed Flashing Steps with Visuals */}
                <section className="space-y-16 sm:space-y-20">
                    <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 sm:gap-16 items-center">
                        <div>
                            <div className="w-12 h-12 sm:w-14 sm:h-14 rounded-2xl bg-tcl-red/10 flex items-center justify-center text-tcl-red mb-6">
                                <Usb size={32} />
                            </div>
                            <h2 className="text-3xl sm:text-4xl font-bold mb-6">Phase 1: USB Media Prep</h2>
                            <div className="space-y-6">
                                <StepItem icon={<ShieldCheck className="text-green-500" />} title="Filesystem: FAT32" desc="TVs will NOT recognize NTFS or exFAT. Use a Windows machine to format. Manual formatting via CMD is safer for larger drives." />
                                <StepItem icon={<Terminal className="text-tcl-red" />} title="Root Directory Only" desc="Do NOT place files inside folders. The TV bootloader looks specifically at the root index of the drive." />
                                <StepItem icon={<Smartphone className="text-orange-500" />} title="The 2.0 Priority" desc="Even on 4K TVs, the USB 2.0 (Black) port is often more stable for bootloader flashing than the USB 3.0 (Blue) port." />
                            </div>
                        </div>
                        <div className="glass aspect-square rounded-[2.5rem] sm:rounded-[3rem] border-white/5 p-8 sm:p-10 flex flex-col items-center justify-center text-center">
                            <div className="w-24 h-32 sm:w-32 sm:h-40 bg-gray-800 rounded-lg border-2 border-tcl-red/30 relative overflow-hidden flex flex-col p-2 gap-2">
                                <div className="w-full h-4 bg-gray-700 rounded" />
                                <div className="w-full h-2 bg-tcl-red/40 rounded" />
                                <div className="w-full h-16 bg-gray-900 rounded border border-white/10 flex items-center justify-center">
                                    <div className="text-[6px] sm:text-[8px] text-gray-400 font-mono italic">V8-T615T03-LF1V555.zip</div>
                                </div>
                            </div>
                            <div className="mt-8 text-xs sm:text-sm text-gray-500 font-bold uppercase tracking-widest">Correct OTA File Placement</div>
                        </div>
                    </div>
                </section>

                {/* Global Reminder */}
                <div className="mt-24 sm:mt-40 p-8 sm:p-10 rounded-[2.5rem] bg-tcl-red/10 border border-tcl-red/20 text-center">
                    <AlertCircle className="mx-auto text-tcl-red mb-6" size={48} />
                    <h3 className="text-xl sm:text-2xl font-bold mb-4">Did the update fail?</h3>
                    <div className="text-gray-600 dark:text-gray-400 max-w-2xl mx-auto leading-relaxed space-y-4 text-sm sm:text-base px-4">
                        <p>
                            90% of failures are due to poor USB drives or incorrect formatting.
                        </p>
                        <p>
                            <strong>Pro Tip:</strong> If your screen is upside down or has weird colors after an IMG flash, you have likely flashed a version with a different Panel ID mapping.
                            Try a different 'LF1Vxxx' revision specifically for your TV size.
                        </p>
                    </div>
                </div>
            </div>
        </div>
    );
};

const StepItem = ({ icon, title, desc }) => (
    <div className="flex gap-4">
        <div className="mt-1">{icon}</div>
        <div>
            <h4 className="font-bold text-gray-900 dark:text-white mb-1">{title}</h4>
            <p className="text-sm text-gray-400 leading-relaxed">{desc}</p>
        </div>
    </div>
);

const ArrowRight = ({ className, size }) => (
    <svg className={className} width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14" /><path d="m12 5 7 7-7 7" /></svg>
);

export default FlashingGuide;
