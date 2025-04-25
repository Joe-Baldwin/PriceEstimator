import { useState, useEffect } from 'react';
import VendorSelect from '../components/VendorSelect';
import MaterialInput from '../components/MaterialInput';
import EstimateTable from '../components/EstimateTable';
import TotalCost from '../components/TotalCost';
import EmailButton from '../components/EmailButton';
import ExportButton from '../components/ExportButton';

export default function EstimatePage() {
  const [vendors, setVendors] = useState([]);
  const [selectedVendor, setSelectedVendor] = useState('');
  const [items, setItems] = useState([]);
  const [selectedItems, setSelectedItems] = useState<any[]>([]);
  const [emailSent, setEmailSent] = useState(false);

  useEffect(() => {
    fetch(`${process.env.NEXT_PUBLIC_API_URL}/vendors`)
      .then(res => res.json())
      .then(data => setVendors(data));
  }, []);

  useEffect(() => {
    if (selectedVendor) {
      fetch(`${process.env.NEXT_PUBLIC_API_URL}/vendors/${selectedVendor}/items`)
        .then(res => res.json())
        .then(data => setItems(data));
    } else {
      setItems([]);
    }
  }, [selectedVendor]);

  const handleEmail = async () => {
    const total = selectedItems.reduce((sum, item) => sum + (item.msrp_price || 0), 0);
    await fetch(`${process.env.NEXT_PUBLIC_API_URL}/email_estimate`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        to_email: 'client@example.com',
        subject: 'Your Estimate',
        items: selectedItems,
        total
      })
    });
    setEmailSent(true);
  };

  const handleExport = () => {
    window.open(`${process.env.NEXT_PUBLIC_API_URL}/export/vendors`, '_blank');
  };

  return (
    <div className="max-w-3xl mx-auto p-8 bg-white shadow rounded mt-8">
      <h2 className="text-2xl font-bold mb-6">Estimate Generator</h2>
      <VendorSelect vendors={vendors} value={selectedVendor} onChange={setSelectedVendor} />
      <div className="my-6">
        <MaterialInput items={items} value={null} onChange={item => setSelectedItems([...selectedItems, item])} />
      </div>
      <EstimateTable items={selectedItems} />
      <TotalCost items={selectedItems} />
      <div className="flex mt-4">
        <EmailButton disabled={selectedItems.length === 0} onClick={handleEmail} />
        <ExportButton disabled={false} onClick={handleExport} />
      </div>
      {emailSent && <div className="text-green-600 mt-2">Estimate emailed!</div>}
    </div>
  );
}
