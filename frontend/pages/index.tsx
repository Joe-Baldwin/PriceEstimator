import Head from 'next/head';
import Link from 'next/link';

export default function Home() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gray-50">
      <Head>
        <title>Price Estimator</title>
      </Head>
      <h1 className="text-4xl font-bold mb-8">Price Estimator</h1>
      <Link href="/estimate" className="px-6 py-3 bg-blue-600 text-white rounded-lg shadow hover:bg-blue-700 transition">Go to Estimates</Link>
    </div>
  );
}
