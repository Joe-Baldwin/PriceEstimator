import React from 'react';

type Vendor = { id: string; name: string };

type Props = {
  vendors: Vendor[];
  value: string;
  onChange: (id: string) => void;
};

const VendorSelect: React.FC<Props> = ({ vendors, value, onChange }) => (
  <div className="mb-4">
    <label className="block mb-1 font-semibold">Vendor</label>
    <select
      className="w-full border rounded px-3 py-2"
      value={value}
      onChange={e => onChange(e.target.value)}
    >
      <option value="">Select a vendor</option>
      {vendors.map(v => (
        <option key={v.id} value={v.id}>{v.name}</option>
      ))}
    </select>
  </div>
);

export default VendorSelect;
