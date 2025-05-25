import React from 'react';

type Item = { code: string; description: string; msrp_price: number };

type Props = {
  items: Item[];
};

const EstimateTable: React.FC<Props> = ({ items }) => (
  <div className="overflow-x-auto mt-4">
    <table className="min-w-full border">
      <thead>
        <tr className="bg-gray-100">
          <th className="px-4 py-2 border">Code</th>
          <th className="px-4 py-2 border">Description</th>
          <th className="px-4 py-2 border text-right">MSRP Price</th>
        </tr>
      </thead>
      <tbody>
        {items.filter(Boolean).map((item, idx) => (
          <tr key={idx}>
            <td className="px-4 py-2 border">{item.code}</td>
            <td className="px-4 py-2 border">{item.description}</td>
            <td className="px-4 py-2 border text-right">{typeof item.msrp_price === 'number' ? `$${item.msrp_price.toFixed(2)}` : ''}</td>
          </tr>
        ))}
      </tbody>
    </table>
  </div>
);

export default EstimateTable;
